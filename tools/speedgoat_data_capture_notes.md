# Speedgoat 数据采集工作流记录

## 当前人工流程

1. 对齐开发机 MATLAB 与 Speedgoat target software 版本。
2. 在 Simulink 中对工程模型执行 Ctrl+B，编译生成 `.mldatx`。
3. 在 SLRT Explorer 中上传刚生成的 `.mldatx`。
4. 在 SLRT Explorer 中运行应用。
5. 如果需要修改参数，也在 SLRT Explorer 中在线修改。

## 本项目采集策略

- 不自动加载、构建、部署或启动 `TestStructure.slx`。
- 外骨骼工程模型的上传、运行、停止和在线调参继续由工程师在 SLRT Explorer 中人工完成。
- 脚本优先负责：
  - 检查 target 连接状态。
  - 导入 Speedgoat File Log。
  - 归档试次日志和元数据。
  - 导出 Python 分析可读取的 CSV 或 MAT。

## 第一批需要记录的信号

- `q_meas`
- `dq_meas`
- `q_ref`
- `dq_ref`
- `FeetLoad`
- `Phi`
- `Phase0Event`
- `tau_e`
- `SafeTorque`
- 助力使能状态
- 参数快照：`Amplitude`、`tau`、`phase_offset`、`MO_Kp`、`MO_Kd`、`MO_OverwriteKpGain`

## 当前已确认

- Target 名称：`TargetPC1`
- Target IP：`192.168.7.99`
- 开发机 USB 网口 IP：`192.168.7.5`
- MATLAB 可以连接 Speedgoat，target 状态可回到 `IDLE`。

## 自生成信号验证

已创建独立 smoke test：

- 脚本：`tools/run_slrt_filelog_smoke_test.m`
- 模型：`tools/generated/slrt_filelog_smoke.slx`
- 应用：`tools/generated/slrt_filelog_smoke.mldatx`
- 轮询结果：`tools/generated/slrt_filelog_smoke_direct_samples.csv`

验证结果：

- 可以编译独立无硬件依赖模型。
- 可以将 `.mldatx` 加载到 `TargetPC1`。
- 可以启动并停止目标机应用。
- 可以通过 `getsignal` 从 Speedgoat 运行中的应用读取自生成信号。
- 当前 `slrealtime.Instrument.getBufferedData` 返回空 map。
- R2023b 的 File Log block 位于 `slrealtimeloglib`，不是 `slrealtimelib`。
- 若要编译出 File Log channel，模型中需要加入 `slrealtimeloglib/Enable File Log`，并把每个待记录信号分支接入 `slrealtimeloglib/File Log`。
- `Enable File Log` 有一个布尔输入端口 `E`；必须接入 `true` 或试次使能信号。只把该 block 放在模型里但悬空输入，会导致 File Log 不能持续记录，通常只导出 1 个样本。
- 加入 File Log block 后，生成的 `loggingdb.json` 已从 `num_entries=0` 变为包含记录 channel，`tg.FileLog.DataAvailable` 也变为 1。
- 连接 `Enable File Log/E=true` 后，最小 File Log 模型已能导出完整多样本时间序列：5 秒、1 kHz、两个通道各 5001 个样本。
- 作为兜底，`getsignal` 轮询已经能稳定从运行中的 Speedgoat 应用读取连续变化的自生成信号，并保存为 CSV；这适合低频状态检查，不适合替代高频步态试次记录。

## MAT 回放验证

用户已将若干 `.mat` 文件放入 `data/inbox/`。这些文件中的主变量 `data` 是 `Simulink.SimulationData.Dataset`，可以用来做安全回放模拟。

已创建独立 MAT 回放脚本：

- 脚本：`tools/run_slrt_mat_playback_test.m`
- 输入：`data/inbox/20260610-male-2.mat`
- 模型：`tools/generated/slrt_mat_playback.slx`
- 应用：`tools/generated/slrt_mat_playback.mldatx`
- 轮询结果：`tools/generated/slrt_mat_playback_polled_samples.csv`
- File Log 导出：`tools/generated/slrt_mat_playback_filelog_export.csv`

当前脚本从原始试次的 18 秒开始截取 12 秒，并回放：

- element 12：`Phi_before_correction` -> `replay_phi`
- element 37：`LeftHipMotorTorque` -> `replay_left_torque`
- element 38：`RightHipMotorTorque` -> `replay_right_torque`

验证结果：

- `.mat` 数据可以转换成 lookup table 形式，编译进独立 SLRT 模型并在 Speedgoat 上播放。
- `getsignal` 轮询可以截取到运行中的回放信号。
- 第二次测试的轮询 CSV 中 `replay_left_torque` 和 `replay_right_torque` 均出现连续变化，例如 `replay_left_torque` 从约 2.50 到 2.08，`replay_right_torque` 在正负小幅范围内变化。
- `replay_phi` 在 0.25 秒间隔轮询点仍为 0，可能是该段相位事件/脉冲没有落在轮询采样点上；这不影响力矩通道回放验证。
- 连接 `Enable File Log/E=true` 后，MAT 回放模型的 File Log 已能导出完整多样本时间序列。当前测试中应用运行约 6.93 秒，decimation=10，三个通道各导出 694 个样本。

## 日志导入与归档

已创建日志归档函数：

- 函数：`tools/import_slrt_filelog_trial.m`
- 示例：
  ```matlab
  addpath('tools');
  import_slrt_filelog_trial('trial_001', 'TestStructure', ...
      SubjectId='subj_001', ...
      AffectedSide='right', ...
      ParameterSnapshotPath='data/raw/trial_001/params.json');
  ```

该函数不会构建、加载、启动或停止外骨骼工程模型。它只连接 `TargetPC1`，从目标机已有 File Log 中选择指定应用的最新 run，导入 SDI，然后归档到：

- `data/raw/<trial_id>/filelog_dataset.mat`
- `data/raw/<trial_id>/signals_long.csv`
- `data/raw/<trial_id>/signals_wide_if_aligned.csv`
- `data/raw/<trial_id>/metadata.json`

已用 `slrt_mat_playback` 的最新 File Log 做过归档测试：

- 输出目录：`data/raw/debug_slrt_mat_playback_001/`
- 信号数：3
- 每个信号样本数：694
- 时间范围：0 到 6.93 秒

## 当前结论

`.mat` 文件可以用于模拟：做法不是让 Speedgoat 运行时直接读取 `.mat` 文件，而是在 MATLAB 端把其中的 timeseries 截取出来，转换为 lookup table 或等价可代码生成的信号源，编译为一个独立 `.mldatx` 后在 Speedgoat 上播放。

目前已确认两条采集路径：

1. 低频轮询路径：`getsignal` 可以从运行中的 Speedgoat 应用读取回放数据，已经验证可用。
2. 正规高频日志路径：File Log block 可以建立通道并导出多样本时间序列，已经在独立最小模型和 MAT 回放模型中验证可用。

下一步建议：

1. 在外骨骼工程模型中只做信号命名和 File Log 分支接入，不改变控制链路。
2. 给 `Enable File Log/E` 接入恒 true 或一个明确的试次记录使能信号。
3. 工程模型仍按用户流程 Ctrl+B 生成 `.mldatx`，再通过 SLRT Explorer 上传、运行和调参。
4. 试次结束后用 `import_slrt_filelog_trial` 导入 File Log，并归档为 `data/raw/<trial_id>/` 下的 MAT/CSV/JSON。
