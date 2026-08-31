"""Export signal candidates from a Simulink .slx file without opening Simulink."""

from __future__ import annotations

import argparse
import csv
import json
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET


RECOMMEND_KEYWORDS = (
    "q_meas",
    "dq_meas",
    "q_ref",
    "dq_ref",
    "FeetLoad",
    "Phi",
    "Phase0Event",
    "tau_e",
    "SafeTorque",
    "Amplitude",
    "phase_offset",
    "MO_Kp",
    "MO_Kd",
    "MO_OverwriteKpGain",
    "Torque",
    "DMP",
    "Phase",
    "Kp",
    "Kd",
)

SEARCH_ONLY_KEYWORDS = (
    "assist",
    "enable",
    "Enabled",
    "Robot",
    "AO",
    "Controller",
)

KEYWORDS = RECOMMEND_KEYWORDS + SEARCH_ONLY_KEYWORDS

@dataclass
class BlockInfo:
    sid: str
    name: str
    block_type: str
    path: str
    parent_path: str
    system_ref: str | None
    port_counts: dict[str, str]


def main() -> int:
    parser = argparse.ArgumentParser(description="Export .slx signal candidates.")
    parser.add_argument("slx_path", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("tools/generated"))
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    payload = export_candidates(args.slx_path)

    json_path = args.output_dir / f"{args.slx_path.stem.lower()}_signal_candidates.json"
    csv_path = args.output_dir / f"{args.slx_path.stem.lower()}_signal_candidates.csv"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(csv_path, payload["candidates"])

    print(f"Exported {payload['total_candidates']} candidates")
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")
    return 0


def export_candidates(slx_path: Path) -> dict:
    with zipfile.ZipFile(slx_path) as archive:
        systems = {
            Path(name).stem: ET.fromstring(archive.read(name))
            for name in archive.namelist()
            if name.startswith("simulink/systems/") and name.endswith(".xml")
        }

    blocks_by_sid: dict[str, BlockInfo] = {}
    system_paths: dict[str, str] = {"system_root": slx_path.stem}
    walk_system(
        systems=systems,
        system_ref="system_root",
        current_path=slx_path.stem,
        blocks_by_sid=blocks_by_sid,
        system_paths=system_paths,
    )

    candidates = []
    for system_ref, system_xml in systems.items():
        parent_path = system_paths.get(system_ref, slx_path.stem)
        for line in system_xml.findall("Line"):
            candidate = line_to_candidate(line, parent_path, blocks_by_sid)
            if candidate is not None:
                candidate["id"] = f"sig_{len(candidates) + 1:04d}"
                candidates.append(candidate)

    payload = {
        "model": slx_path.stem,
        "source_slx": str(slx_path),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "method": "static_slx_xml_parse",
        "note": (
            "This is a static XML parse of the .slx file. It does not compile, "
            "deploy, or start the model. Protected model internals remain opaque."
        ),
        "recommended_keywords": list(RECOMMEND_KEYWORDS),
        "search_only_keywords": list(SEARCH_ONLY_KEYWORDS),
        "total_blocks": len(blocks_by_sid),
        "total_candidates": len(candidates),
        "candidates": candidates,
        "groups": summarize_groups(candidates),
    }
    return payload


def walk_system(
    systems: dict[str, ET.Element],
    system_ref: str,
    current_path: str,
    blocks_by_sid: dict[str, BlockInfo],
    system_paths: dict[str, str],
) -> None:
    system_xml = systems.get(system_ref)
    if system_xml is None:
        return

    for block in system_xml.findall("Block"):
        sid = block.attrib.get("SID", "")
        name = block.attrib.get("Name", "")
        block_type = block.attrib.get("BlockType", "")
        path = f"{current_path}/{name}" if name else current_path
        child_system_ref = None
        system_child = block.find("System")
        if system_child is not None:
            child_system_ref = system_child.attrib.get("Ref")
        port_counts_node = block.find("PortCounts")
        port_counts = dict(port_counts_node.attrib) if port_counts_node is not None else {}
        if sid:
            blocks_by_sid[sid] = BlockInfo(
                sid=sid,
                name=name,
                block_type=block_type,
                path=path,
                parent_path=current_path,
                system_ref=child_system_ref,
                port_counts=port_counts,
            )
        if child_system_ref:
            system_paths[child_system_ref] = path
            walk_system(systems, child_system_ref, path, blocks_by_sid, system_paths)


def line_to_candidate(
    line: ET.Element,
    parent_path: str,
    blocks_by_sid: dict[str, BlockInfo],
) -> dict | None:
    properties = {
        prop.attrib.get("Name", ""): prop.text or ""
        for prop in line.findall("P")
    }
    src = properties.get("Src", "")
    if not src:
        return None
    src_sid, src_port = parse_endpoint(src)
    if not src_sid:
        return None
    src_block = blocks_by_sid.get(src_sid)
    if src_block is None:
        return None

    dst_values = [properties.get("Dst", "")] + [branch_dst for branch_dst in branch_dsts(line)]
    dst_blocks = []
    dst_types = []
    for dst in dst_values:
        dst_sid, _ = parse_endpoint(dst)
        if dst_sid and dst_sid in blocks_by_sid:
            dst_block = blocks_by_sid[dst_sid]
            dst_blocks.append(dst_block.path)
            dst_types.append(dst_block.block_type)

    signal_name = properties.get("Name", "").strip()
    group_path = group_for_path(src_block.path)
    search_text = " ".join([signal_name, src_block.path, src_block.block_type, " ".join(dst_blocks)])
    hits = [keyword for keyword in KEYWORDS if keyword.lower() in search_text.lower()]
    recommend_hits = [
        keyword
        for keyword in RECOMMEND_KEYWORDS
        if keyword.lower() in search_text.lower()
    ]

    return {
        "signal_name": signal_name,
        "source_block": src_block.path,
        "source_name": src_block.name,
        "source_block_type": src_block.block_type,
        "source_port": src_port,
        "parent_path": parent_path,
        "group_path": group_path,
        "destination_count": len(dst_blocks),
        "destination_blocks": dst_blocks,
        "destination_block_types": dst_types,
        "keyword_hits": hits,
        "recommendation_hits": recommend_hits,
        "recommended": bool(recommend_hits),
        "is_named": bool(signal_name),
    }


def parse_endpoint(endpoint: str) -> tuple[str, str]:
    if "#" not in endpoint:
        return "", ""
    sid, port = endpoint.split("#", 1)
    return sid, port


def branch_dsts(line: ET.Element) -> list[str]:
    dsts: list[str] = []
    for branch in line.findall(".//Branch"):
        for prop in branch.findall("P"):
            if prop.attrib.get("Name") == "Dst" and prop.text:
                dsts.append(prop.text)
    return dsts


def group_for_path(path: str) -> str:
    parts = path.split("/")
    if len(parts) <= 2:
        return parts[0]
    return "/".join(parts[: min(len(parts) - 1, 4)])


def summarize_groups(candidates: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for candidate in candidates:
        grouped[candidate["group_path"]].append(candidate)
    return [
        {
            "group_path": group,
            "candidate_count": len(items),
            "recommended_count": sum(1 for item in items if item["recommended"]),
        }
        for group, items in sorted(grouped.items(), key=lambda pair: pair[0].lower())
    ]


def write_csv(path: Path, candidates: list[dict]) -> None:
    fieldnames = [
        "id",
        "recommended",
        "signal_name",
        "source_block",
        "source_block_type",
        "source_port",
        "group_path",
        "destination_count",
        "destination_blocks",
        "keyword_hits",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for candidate in candidates:
            row = dict(candidate)
            row["destination_blocks"] = " | ".join(candidate["destination_blocks"])
            row["keyword_hits"] = " | ".join(candidate["keyword_hits"])
            writer.writerow({key: row.get(key, "") for key in fieldnames})


if __name__ == "__main__":
    raise SystemExit(main())
