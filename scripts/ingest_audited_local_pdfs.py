from __future__ import annotations

from pathlib import Path

from pipeline_utils import PAPERS, RAW, clean_text, load_json, normalize_doi, save_json


ROOT = Path(__file__).resolve().parents[1]
DISPOSITION = ROOT / "outputs" / "orphan_pdf_disposition.md"


AUDITED_PAPERS = [
    {
        "title": "Model Mediated Teleoperation with a Hand-Arm Exoskeleton in Long Time Delays Using Reinforcement Learning",
        "year": 2020,
        "venue": "IEEE RO-MAN",
        "doi": "10.1109/RO-MAN47096.2020.9223477",
        "filename": "2020_Model_Mediated_Teleoperation_with_a_Hand-Arm_Exoskeleton_in_Long_Time__10.1109_ro-man47096.2020.9223477.pdf",
        "keywords": ["exoskeleton", "reinforcement learning", "dynamic movement primitives", "teleoperation"],
        "query": "audited local PDF: DMP and reinforcement learning",
        "local_role": "supporting_cross_domain",
    },
    {
        "title": "Shortcomings of human-in-the-loop optimization of an ankle-foot prosthesis emulator: a case series",
        "year": 2021,
        "venue": "Royal Society Open Science",
        "doi": "10.1098/rsos.202020",
        "filename": "2020_Shortcomings_of_human-in-the-loop_optimization_for_an_ankle-foot_prost_10.1101_2020.10.17.343970.pdf",
        "keywords": ["human-in-the-loop optimization", "prosthesis", "limitations", "wearable robot"],
        "query": "audited local PDF: HIL optimization limitations",
        "local_role": "core_counterevidence",
    },
    {
        "title": "A Pediatric Knee Exoskeleton With Real-Time Adaptive Control for Overground Walking in Ambulatory Individuals With Cerebral Palsy",
        "year": 2021,
        "venue": "Frontiers in Robotics and AI",
        "doi": "10.3389/frobt.2021.702137",
        "filename": "2021_A_Pediatric_Knee_Exoskeleton_With_Real-Time_Adaptive_Control_for_Overg_10.3389_frobt.2021.702137.pdf",
        "keywords": ["knee exoskeleton", "adaptive control", "gait", "rehabilitation"],
        "query": "audited local PDF: knee exoskeleton adaptive control",
        "local_role": "core_control_reference",
    },
    {
        "title": "Explaining Bayesian Optimization by Shapley Values Facilitates Human-AI Collaboration",
        "year": 2024,
        "venue": "arXiv",
        "doi": "10.48550/arXiv.2403.04629",
        "filename": "2024_Explaining_Bayesian_Optimization_by_Shapley_Values_Facilitates_Human-A_10.48550_arxiv.2403.04629.pdf",
        "keywords": ["bayesian optimization", "explainability", "human-AI collaboration"],
        "query": "audited local PDF: explainable Bayesian optimization",
        "local_role": "supporting_optimizer_reference",
    },
    {
        "title": "Novel Design on Knee Exoskeleton with Compliant Actuator for Post-Stroke Rehabilitation",
        "year": 2025,
        "venue": "Sensors",
        "doi": "10.3390/s25010153",
        "filename": "2024_Novel_Design_on_Knee_Exoskeleton_with_Compliant_Actuator_for_Post-Stro_10.3390_s25010153.pdf",
        "keywords": ["knee exoskeleton", "compliant actuator", "stroke rehabilitation", "safety"],
        "query": "audited local PDF: knee exoskeleton compliant actuation",
        "local_role": "supporting_hardware_reference",
    },
    {
        "title": "Design optimization platform for assistive wearable devices applied to a knee damper exoskeleton",
        "year": 2025,
        "venue": "Wearable Technologies",
        "doi": "10.1017/wtc.2025.10016",
        "filename": "2025_Design_optimization_platform_for_assistive_wearable_devices_applied_to_10.1017_wtc.2025.10016.pdf",
        "keywords": ["design optimization", "wearable device", "knee exoskeleton", "human-in-the-loop"],
        "query": "audited local PDF: exoskeleton design optimization",
        "local_role": "core_optimizer_reference",
    },
    {
        "title": "Portable hip exoskeleton improves walking economy for stroke survivors",
        "year": 2026,
        "venue": "Nature Communications",
        "doi": "10.1038/s41467-026-69580-0",
        "filename": "s41467-026-69580-0.pdf",
        "keywords": ["hip exoskeleton", "stroke", "walking economy", "wearable robot"],
        "query": "audited local PDF: mentor-provided exoskeleton reference",
        "local_role": "mentor_reference",
    },
    {
        "title": "Therapist-exoskeleton-patient interaction for gait therapy",
        "year": 2026,
        "venue": "Science Robotics",
        "doi": "10.1126/scirobotics.adz9628",
        "filename": "scirobotics.adz9628.pdf",
        "keywords": ["exoskeleton", "therapist interaction", "gait therapy", "stroke rehabilitation"],
        "query": "audited local PDF: mentor-provided exoskeleton reference",
        "local_role": "mentor_reference",
    },
    {
        "title": "基于在线增量DMP的准直驱膝关节外骨骼自适应柔顺控制",
        "year": 2026,
        "venue": "仪器仪表学报",
        "doi": "10.19650/j.cnki.cjsi.J2614961",
        "filename": "基于在线增量DMP的准直驱膝关节外骨骼自适应柔顺控制.pdf",
        "keywords": ["膝关节外骨骼", "动态运动基元", "在线增量学习", "自适应柔顺控制"],
        "query": "audited local PDF: user prior work and project foundation",
        "local_role": "user_prior_work",
    },
]


EXCLUDED_FILES = [
    {
        "filename": "2022_Ultra-Robust_Real-Time_Estimation_of_Gait_Phase_10.1109_tnsre.2022.3207919_1.pdf",
        "reason": "重复副本；同 DOI 的规范文件已与矩阵记录关联。",
    },
    {
        "filename": "2023_Learning_to_Assist_Different_Wearers_in_Multitasks_Efficient_and_Indiv_10.48550_arxiv.2309.14720.pdf",
        "reason": "早期 arXiv 版本；矩阵已保留同一工作的 2024 年 IEEE Transactions on Robotics 期刊版。",
    },
    {
        "filename": "2021_Self-adaptive_Particle_Swarm_Optimization_with_Human-in-the-loop_for_A_10.18494_sam.2021.3227.pdf",
        "reason": "文件内容是 Sensors and Materials 投稿说明，不是题名所示论文，禁止作为论文证据入库。",
    },
]


def key_for(paper: dict) -> str:
    return normalize_doi(paper.get("doi")) or clean_text(paper.get("title")).lower()


def main() -> None:
    papers = load_json(RAW / "papers_with_pdf_status.json", [])
    by_key = {key_for(paper): paper for paper in papers if key_for(paper)}
    added = 0
    updated = 0

    for audited in AUDITED_PAPERS:
        path = (PAPERS / audited["filename"]).resolve()
        if not path.is_file():
            raise SystemExit(f"Audited PDF is missing: {path}")
        payload = {key: value for key, value in audited.items() if key != "filename"}
        payload.update(
            {
                "url": f"https://doi.org/{normalize_doi(audited['doi'])}",
                "pdf_path": str(path),
                "pdf_status": "manual_pdf",
                "pdf_source_note": "audited_local_pdf",
            }
        )
        key = key_for(payload)
        if key in by_key:
            by_key[key].update(payload)
            updated += 1
        else:
            papers.append(payload)
            by_key[key] = payload
            added += 1

    save_json(RAW / "papers_with_pdf_status.json", papers)

    lines = [
        "# 本地未关联 PDF 处置记录",
        "",
        "## 已补入矩阵语料",
        "",
    ]
    for paper in AUDITED_PAPERS:
        lines.append(
            f"- {paper['title']} | DOI: {paper['doi']} | local_role: `{paper['local_role']}` | "
            f"`{paper['filename']}`"
        )
    lines.extend(["", "## 不作为独立矩阵记录", ""])
    for item in EXCLUDED_FILES:
        lines.append(f"- `{item['filename']}`：{item['reason']}")
    DISPOSITION.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"metadata={len(papers)} added={added} updated={updated}")
    print(f"disposition={DISPOSITION.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
