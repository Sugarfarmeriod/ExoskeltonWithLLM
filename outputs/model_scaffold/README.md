# MS-TGSS Model Scaffold

This folder contains a runnable PyTorch scaffold for the MS-TGSS model:

- `dataset.py`: CSV/MAT table loading, sliding windows, standardization.
- `features.py`: derived signals, weak labels, synthetic anomaly injection, rule gate.
- `model_tcn_multitask.py`: TCN + attention pooling + four multitask heads.
- `train.py`: training loop and checkpoint saving.
- `evaluate.py`: metrics plus Simulink playback CSV export.
- `export_onnx.py`: ONNX export.

## Expected CSV Columns

Export one table per trial from MATLAB/Simulink/Speedgoat with these columns:

```text
q_meas,dq_meas,q_ref,dq_ref,tau_e,FeetLoad_left,FeetLoad_right,Phi,Phase0Event
```

The scaffold adds:

```text
e_q,e_dq,sin_Phi,cos_Phi,FeetLoad_sum,FeetLoad_diff,moving RMS/peak/slope features
```

## Install

From this folder or the project root:

```bash
pip install torch pandas numpy scikit-learn scipy onnx
```

`scipy` is only needed if you adapt `read_table()` for MAT files. CSV is the recommended first path.

## Train

Replace paths with real exported trial files:

```bash
python outputs/model_scaffold/train.py \
  --train data/trial01.csv,data/trial02.csv \
  --val data/trial03.csv \
  --out-dir outputs/model_scaffold/runs/ms_tgss \
  --raw-hz 1000 \
  --target-hz 100 \
  --window-ms 400 \
  --stride-ms 50 \
  --inject-anomalies
```

Checkpoint:

```text
outputs/model_scaffold/runs/ms_tgss/best_model.pt
```

## Evaluate and Export Simulink Playback CSV

```bash
python outputs/model_scaffold/evaluate.py \
  --checkpoint outputs/model_scaffold/runs/ms_tgss/best_model.pt \
  --data data/trial04.csv \
  --out-dir outputs/model_scaffold/runs/eval_trial04
```

Outputs:

```text
metrics.txt
simulink_playback_predictions.csv
```

The playback CSV contains:

```text
gait_state_pred, anomaly_type_pred, risk_level_pred,
gate_gain_pred, gate_gain_rule, gate_gain_final, tau_e, tau_gate
```

Use `tau_gate` as the replay signal between `TorqueController` and `Torque_Guard`.

## Export ONNX

```bash
python outputs/model_scaffold/export_onnx.py \
  --checkpoint outputs/model_scaffold/runs/ms_tgss/best_model.pt \
  --out outputs/model_scaffold/runs/ms_tgss/ms_tgss.onnx
```

## Label IDs

`gait_state`:

- `0`: stance
- `1`: swing
- `2`: transition

`anomaly_type`:

- `0`: normal
- `1`: phase_mismatch
- `2`: tracking_error
- `3`: torque_risk
- `4`: footload_inconsistency
- `5`: sensor_fault

`risk_level`:

- `0`: normal
- `1`: caution
- `2`: danger

## Safety Rule

The model predicts `gate_gain_pred`, but deployment should use:

```text
gate_gain_final = min(gate_gain_pred, gate_gain_rule)
tau_gate = gate_gain_final * tau_e
```

Danger forces `gate_gain_final = 0`. Caution clips the final gain to `0.3-0.7`. Normal allows up to `1.0`.

## First Real-data Adaptation Steps

1. Export a short normal walking trial as CSV with the expected columns.
2. Check units and signs for `q_meas`, `q_ref`, `tau_e`, and `FeetLoad`.
3. Tune `contact_threshold`, `safe_torque`, `tracking_error_q`, and `tracking_error_dq` in `FeatureConfig`.
4. Train with `--inject-anomalies`.
5. Inspect `simulink_playback_predictions.csv` before connecting any closed-loop branch.
