# InterForceControlTask 可调参数整理

来源模型：`TestStructure.slx`

范围：只递归检查 `TestStructure/InterForceControlTask` 及其子模块。模型加载时 MATLAB 提示缺少 `Robot2.slxp`、`BaseController.slxp`，本报告基于当前 `.slx` 内可读取内容生成。

事实校正：`TestStructure.slx` 是当前正式外骨骼实验模型。当前 `AO` 的相位与事件估计仅依赖足底压力；它不是既有中文论文中 AFO 的后续版本。模型中即使保留 `q` 端口或连线，也不得据此把当前 AO 解读为基于关节运动的估计器。本论文和系统实现不使用 EMG 或 IMU；`sEMGMuxIn` 只是承载足底压力/电压的历史端口名。

## 1. InterForceControlTask 主流程理解

`InterForceControlTask` 大体是：

1. `Bus Selector` 从机器人总线取左右膝关节实际位置、速度和传感器 AD。
2. `FootSwitch` 根据 `MO_<WhichFoot>` 选择用于控制的腿侧，把左右实际位置/速度切成当前控制对象的 `q/dq`。
3. `AO` 仅从足底压力信号提取接触/步态事件，估计步态频率 `Omega`、相位 `Phi`、相位零点事件 `Phase0Event`，并输出 `FeetLoad`。模型中保留的 `q` 接口不构成当前 AO 的估计依据。
4. `DMP` 根据 `q/Omega/Phi/Phase0Event` 在线学习并生成参考轨迹 `y/v/PlaybackPhi`。
5. `TorqueController` 对 `q_ref/dq_ref` 与 `q_meas/dq_meas` 做 PD 型误差控制，同时用步态活动检测和步数斜坡管理输出力矩 `tau_e`。
6. 顶层的 `MO_GiveTorque?` 可在真实力矩和 0 之间切换；`Torque_Guard` 再根据足底负载、腿侧、关节位置等做最终安全门控/限幅。
7. 顶层 `Saturation/Saturation1` 把左右输出限制在 `[-20, 20]` 后写入输出总线。

## 2. 明确带 MO_ 前缀的块

| 名称 | 位置 | 类型/当前值 | 作用理解 |
|---|---|---:|---|
| `MO_<WhichFoot>` | 顶层 | Constant, `1` | 选择当前控制/监控的腿侧，送入 `AO`、`FootSwitch`、`Torque_Guard`。会影响用哪条腿的实际位置速度、足底负载/力矩保护逻辑。 |
| `MO_PhaseBias` | 顶层 | Constant, `0` | 输入 `AO`，用于给步态相位估计加偏置；改变相位零点/事件对齐。 |
| `MO_GiveTorque?` | 顶层 | ManualSwitch, `sw=0` | 力矩总开关：在 `MO_OverwriteKpGain` 后的控制力矩与 `MO_Zero=0` 之间切换，再送 `Torque_Guard`。Speedgoat 上应当作为最关键的上电/撤力开关之一。 |
| `MO_Zero` | 顶层 | Constant, `0` | 给 `MO_GiveTorque?` 的零力矩支路，用于关闭输出。 |
| `MO_OverwriteKpGain` | 顶层 | Gain, `1.5` | 对 `TorqueController` 输出的 `tau_e` 做总倍率放大，再进入力矩开关。虽然名字像 Kp 覆盖，实际连接上是整体控制力矩倍率。 |
| `MO_RightCurrentAmplifyGain` | 顶层 | Gain, `0.8/0.7` | 对 `Torque_Guard` 输出的右侧通道再做比例补偿，然后与另一支路汇合到输出。看起来是右侧电流/力矩标定补偿。 |
| `MO_AOActivityThreadhold` | `AO/Select` | Constant, `0.8` | AO 事件选择/活动检测阈值，进入 `If1`。阈值越高，AO 认为“活动有效”的条件越严格。 |
| `MO_AOActivityMovment` | `AO/Select` | Sum | 由 `Moving Average1` 与 `Gain3(0.4)` 组合成 AO 活动量，送 `If1` 与阈值比较。这个更像可监控中间量，不是直接数值参数。 |
| `MO_ActivtyThreadhold` | `TorqueController` | Constant, `0.1` | TorqueController 内活动检测阈值，决定是否认为当前运动/步态活动足够，从而影响后面的活动门控。 |
| `MO_ActivityMovent` | `TorqueController` | Sum | TorqueController 内活动量信号，由移动平均与 `Gain3(0.4)` 组合后进 `If`。更像运行时监控量。 |
| `MO_AutoDisable?` | `TorqueController` | ManualSwitch, `sw=0` | 在固定 `Activity_Enable=1` 与 `Activity gate` 之间切换，送入 `TorqueManager`。用于选择“始终允许”还是“按活动检测自动禁用/启用”。 |
| `MO_Kp` | `TorqueController` | Gain, `0.3` | 位置误差 `Sum_e_q` 的比例增益，和 `MO_Kd` 相加形成 PD 控制项。 |
| `MO_Kd` | `TorqueController` | Gain, `0.005` | 速度误差 `Sum_e_dq` 的微分/阻尼增益，和 `MO_Kp` 相加形成 PD 控制项。 |
| `MO_step ramp ? per 5` | `TorqueController/TorqueManager` | Gain, `1` | 把 `step_count 0..5` 转成 `base_gain 0..1` 前的斜坡增益。当前每 5 步爬升到 1，用来让力矩逐步接入。 |
| `MO_drop ? steps` | `TorqueController/TorqueManager` | Gain, `0` | 活动下降沿进入 `count + step` 的步数调整项。当前为 0，表示掉活动时不额外改变步数计数/斜坡。 |
| `MO_HealthLegdefault` | `Torque_Guard` | Constant, `4.5` | 进入 `MinimumTauGate` 以及左右 `Switch/Switch1`，像是健康腿/支撑腿的默认最小力矩或保护基准值。需要结合实物方向确认正负号和单位。 |

## 3. 带 MO_ 前缀的监控信号

| 信号名 | 来源 | 去向/意义 |
|---|---|---|
| `MO_DMPStepCunter` | `TorqueController/MATLAB Function2` | DMP/步态步数计数监控信号；名字里 `Cunter` 应为 `Counter` 拼写问题。 |
| `MO_currentgain` | `TorqueController/TorqueManager` | 当前 TorqueManager 输出的接入力矩倍率，适合 Speedgoat 实时监控力矩是否按步数 ramp up。 |
| `MO_DMPPhase0Event` | `TorqueController/Subsystem2` | DMP 相位零点事件，进入 `MATLAB Function1/2` 与 `TorqueManager`，用于步态峰值/步数/斜坡管理。 |

## 4. 疑似可调但未加 MO_ 前缀的重点候选

这些项不一定都需要开放到 Speedgoat，但建议你逐项筛选；有些是算法常量，有些是安全保护值，有些只是内部固定逻辑。

| 名称 | 位置 | 当前值 | 建议判断 |
|---|---|---:|---|
| `TBaseDefault` | `AO` | `2.2` | AO 默认步态周期，冷启动/未获得 3 个有效周期前使用。可调。 |
| `TBaseDefault` | `DMP` | `2.2` | DMP 相位/延迟默认周期。最好与 AO 默认周期一致。可调。 |
| `Gain` | `AO` | `0.01` | AO 足底压力/电压输入缩放，送 `AO/Select` 与足底检测分支。候选。 |
| `Gain1` | `AO/Select` | `0.6` | AO Select 内加权项。候选。 |
| `Gain2` | `AO/Select` | `1` | AO Select 偏置/增益项。候选优先级较低。 |
| `Gain3` | `AO/Select` | `0.4` | AO 活动量计算的一部分，和 `MO_AOActivityMovment` 直接相关。建议加 MO 或确认固定。 |
| `LeftLowPass` | `AO/Subsystem1/Detector1` | Num `0.05`, Den `[1 -0.95]` | 足底负载低通滤波，影响触地事件稳定性。可调但要谨慎。 |
| `Amplitude` | `DMP` | `1.0` | DMP 输出形状幅值倍率，直接影响参考轨迹幅度。强候选。 |
| `tau` | `DMP` | `1.0` | DMP 时间缩放参数，影响轨迹播放速度/相位延迟缩放。强候选。 |
| `phase_offset` | `DMP` | `0.5` | DMP 事件/相位延迟偏移，影响辅助时机。强候选。 |
| `iner_phase_offset` | `DMP` | `0` | 输入 DMP 生成函数的内部相位偏置。候选。 |
| `alpha_x1` | `DMP` | `1.0` | DMP canonical system 衰减参数，影响基函数相位分布/轨迹形状。算法参数，谨慎开放。 |
| `alpha_z1` | `DMP` | `25.0` | DMP spring-damper 动态参数，影响轨迹收敛/平滑性。算法参数，谨慎开放。 |
| `Chunksize_manual` | `DMP` | `10` | DMP 增量学习每 tick 处理样本数。实时计算负载相关，Speedgoat 上可监控/调试。 |
| `ComputeTicks` | `DMP` | `1` | DMP 学习计算使能 tick。通常固定。 |
| `MinBasePeriod` | `DMP/Subsystem` | `0.005` | DMP 基准周期下限保护。通常固定。 |
| `dt1` | `DMP/Subsystem` | `0.001` | DMP 延迟/相位重建采样时间。应与任务周期一致，不建议在线乱调。 |
| `Switch3` | 顶层 | Threshold `0` | 由 `ref_q_max` 控制给 TorqueController 的参考切换，需确认是否测试遗留。 |
| `ref_q_max` | 顶层 | `0` | 输入顶层 `Switch3` 的参考选择阈值/控制值，当前为 0。可能是遗留调试项。 |
| `Saturation` | 顶层 | `[-20, 20]` | 输出通道限幅。安全相关，建议明确命名并保留可查。 |
| `Saturation1` | 顶层 | `[-20, 20]` | 另一输出通道限幅。安全相关，建议明确命名并保留可查。 |
| `Activity_Enable` | `TorqueController` | `1` | `MO_AutoDisable?` 的常开支路。候选，但已有开关间接控制。 |
| `Gain` | `TorqueController` | `0.01` | TorqueController 内输入缩放/事件检测相关，候选。 |
| `Gain3` | `TorqueController` | `0.4` | TorqueController 活动量计算的一部分，和 `MO_ActivityMovent` 直接相关。建议加 MO 或确认固定。 |
| `threadhold` | `TorqueController/Subsystem2` | `0.1` | 子系统内阈值，名字拼写为 `threadhold`，可能与事件检测有关。建议筛选。 |
| `step_count 0..5` | `TorqueController/TorqueManager` | Saturate `[0, 5]` | 力矩渐入步数窗口；与 `MO_step ramp ? per 5` 配套。强候选。 |
| `base_gain 0..1` | `TorqueController/TorqueManager` | Saturate `[0, 1]` | 力矩渐入倍率限幅；建议监控。 |
| `LeftLowPass` | `Torque_Guard` | Num `0.05`, Den `[1 -0.95]` | Torque_Guard 内足底负载/接触滤波。可调但安全相关。 |
| `SafeTorque` | `Torque_Guard/LimitProtect` | `20` | 限位保护时的安全力矩/力矩上限相关。强候选，建议加 MO 前缀或明确不可在线调。 |
| `Gain/Gain1` | `Torque_Guard/LimitProtect` | `-1` / `-1` | 左右方向符号翻转，通常由机构方向决定，不建议在线调。 |

完整候选表已导出到 `analysis_outputs/interforce_non_mo_candidates.csv`，共 152 行。

## 5. 建议优先开放/监控的调参组

| 组 | 推荐项 |
|---|---|
| 安全与总开关 | `MO_GiveTorque?`, `MO_Zero`, 顶层 `Saturation/Saturation1`, `SafeTorque`, `MO_HealthLegdefault` |
| 腿侧/相位 | `MO_<WhichFoot>`, `MO_PhaseBias`, `TBaseDefault`, `phase_offset`, `tau` |
| DMP 轨迹 | `Amplitude`, `tau`, `alpha_x1`, `alpha_z1`, `Chunksize_manual`, `PlaybackPhi` |
| PD 控制 | `MO_Kp`, `MO_Kd`, `MO_OverwriteKpGain` |
| 自动启停/渐入 | `MO_AutoDisable?`, `MO_ActivtyThreadhold`, `MO_ActivityMovent`, `MO_step ramp ? per 5`, `MO_currentgain`, `MO_DMPPhase0Event`, `MO_DMPStepCunter` |
| AO 事件检测 | `MO_AOActivityThreadhold`, `MO_AOActivityMovment`, `AO/Select/Gain3`, `AO/Subsystem1/Detector1/LeftLowPass` |

## 6. 命名/整理建议

1. `Threadhold/Activty/Movment/Cunter` 这些拼写建议统一为 `Threshold/Activity/Movement/Counter`，不然 Speedgoat 监控列表里后期很难搜。
2. 真正希望在线可调的项建议统一改成 `MO_` 前缀；只想监控的信号也建议保留 `MO_`，但可以在名字里加 `_mon` 或 `_scope` 区分。
3. 当前最像“漏加 MO”的高优先级项是：`Amplitude`、`tau`、`phase_offset`、两个 `TBaseDefault`、`SafeTorque`、顶层输出限幅、`TorqueManager/step_count 0..5`、两个 `LeftLowPass` 滤波参数。

## 7. 关键输入/输出信号汇总

### 7.1 InterForceControlTask 外部输入

| 输入 | 来源/类型 | 在本子系统中的用途 |
|---|---|---|
| `BusIn` | 机器人/底层硬件状态总线 | 被 `Bus Selector` 拆出左右膝关节位置、速度、传感器 AD 通道。 |
| `sEMGMuxIn` | 外部 8 路传感器向量，模型里作为 `p8` 使用 | 进入 `AO/Subsystem1/Detector1/VoltageToFootLoad`，用于计算左右足底负载和触地事件。虽然名字像 sEMG，但在当前 `VoltageToFootLoad` 代码里按压力/电压通道处理。 |
| `Enable` | EnablePort | 使能整个 `InterForceControlTask` 子系统。 |

### 7.2 Bus Selector 拆出的左右腿/传感器信号

| Bus 信号 | 去向 | 作用 |
|---|---|---|
| `LeftHipMotorActuralPosition` | `FootSwitch`、`Model`、`Torque_Guard` | 左膝实际位置；用于腿侧选择后的 `q_meas/q`，也进入限位保护。名称里 `Actural` 应为 `Actual`。 |
| `LeftHipMotorActuralVelocity` | `FootSwitch`、`Model` | 左膝实际速度；用于腿侧选择后的 `dq_meas`。 |
| `LeftHipMotorSensorADCh1` | 顶层 `Sum2` | 左侧电机传感器 AD 通道，参与最终左侧输出支路的叠加/补偿。 |
| `RightHipMotorActuralPosition` | `FootSwitch`、`Model`、`Torque_Guard` | 右膝实际位置；用于腿侧选择后的 `q_meas/q`，也进入限位保护。 |
| `RightHipMotorActuralVelocity` | `FootSwitch`、`Model` | 右膝实际速度；用于腿侧选择后的 `dq_meas`。 |
| `RightHipMotorSensorADCh1` | 顶层 `Sum1` | 右侧电机传感器 AD 通道，和 `MO_RightCurrentAmplifyGain` 后的右侧力矩/电流支路汇合。 |

### 7.3 FootSwitch 腿侧选择信号

| 信号 | 输入来源 | 输出/用途 |
|---|---|---|
| `LeftHipMotorActuralPosition` | Bus Selector | `MO_<WhichFoot>` 选择为左腿时，输出为 `ActuralPosition`，并参与 `q` 向量。 |
| `LeftHipMotorActuralVelocity` | Bus Selector | `MO_<WhichFoot>` 选择为左腿时，输出为 `ActuralVelocity`。 |
| `RightHipMotorActuralPosition` | Bus Selector | `MO_<WhichFoot>` 选择为右腿时，输出为 `ActuralPosition`，并参与 `q` 向量。 |
| `RightHipMotorActuralVelocity` | Bus Selector | `MO_<WhichFoot>` 选择为右腿时，输出为 `ActuralVelocity`。 |
| `MO_<WhichFoot>` / `<FootSelect>` | 顶层常数 | 控制 `Switch1/Switch2`，决定当前控制对象使用左腿还是右腿。 |
| `ActuralPosition` | FootSwitch 输出 | 送 `TorqueController/q_meas`。 |
| `ActuralVelocity` | FootSwitch 输出 | 送 `TorqueController/dq_meas`。 |
| `q` | FootSwitch 输出 Mux | 连线同时送到 `AO/q` 和 `DMP/q`；其中 DMP 用于轨迹学习/生成，而 `AO/q` 是保留接口，当前 AO 不以关节运动作为相位估计依据。 |

### 7.4 压力/足底负载信号链路

| 信号/模块 | 当前处理 | 用途 |
|---|---|---|
| `sEMGMuxIn` | 进入 `AO/Subsystem1`，再作为 `p8` 进入 `Detector1/VoltageToFootLoad` | 当前模型中实际承担 8 路足底压力/电压输入。 |
| `p8` | 8 路向量输入 | `VoltageToFootLoad` 内部先转 double 并按列向量处理。 |
| `baseline` | 固定 `2.6 * ones(8,1)` | 压力/负载换算基线。负载计算为 `max(baseline - p, 0)`。 |
| 左脚压力通道 | `leftIdx = [2 3]` | `leftLoad = sum(load([2 3]))`。 |
| 右脚压力通道 | `rightIdx = [6 7]` | `rightLoad = sum(load([6 7]))`。 |
| 无效通道保护 | 若对应通道 `p(k)` 非有限值或 `p(k) <= 0.1`，该通道负载置 0 | 避免断线/异常低电压造成误触地。 |
| `LeftLoad` | `VoltageToFootLoad` 输出 1 | 进入 `Detector1/Switch` 和 `AO/Subsystem1/Mux`。 |
| `RightLoad` | `VoltageToFootLoad` 输出 2 | 进入 `Detector1/Switch` 和 `AO/Subsystem1/Mux`。 |
| `Whichfoot` | 来自 `MO_<WhichFoot>` | 在 `Detector1/Switch` 中选择用于触地事件检测的左/右负载。 |
| `LeftLowPass` | 离散传函 Num `0.05`, Den `[1 -0.95]` | 对选中的足底负载低通滤波。 |
| `ContactRelay` | Relay | 将滤波后的负载变成接触/站立逻辑。 |
| `RisingEdge` | 与 `PrevContact` 比较 | 检测触地上升沿。 |
| `Phase0Event` | `EventToDouble` 输出 | 作为 AO 内部步态零相位事件，再经 `ColdStartEventGate` 输出到 DMP。 |
| `FeetLoad` | `[LeftLoad, RightLoad]` Mux | 输出到 `Torque_Guard`，用于站立/支撑相关安全门控。 |

### 7.5 AO 到 DMP 的步态相位信号

| AO 输出 | 去向 | 作用 |
|---|---|---|
| `FeetLoad` | `Torque_Guard` | 左右足底负载向量，用于安全门控、最小力矩门和站立判断。 |
| `x` | 当前顶层无明显去向 | AO 内部保留输出，可能是调试/历史信号。 |
| `Omega` | `DMP/Omega` | 步态频率估计；AO 的 `PhaseCorrection` 根据有效事件和默认周期估计。 |
| `Phi` / `Phi_before_correction` | `DMP/Phi`、顶层 `Gain` | 步态相位，DMP 用它推进或对齐轨迹。 |
| `Phase0Event` | `DMP/Phase0Event` | 步态零点/触地事件，触发 DMP 学习窗口、参数锁存、播放重置等逻辑。 |

### 7.6 DMP 到 TorqueController 的参考信号

| DMP 输出 | 去向 | 作用 |
|---|---|---|
| `y` | 顶层 `Switch3`，再作为 `y_limited` 到 `TorqueController/q_ref` | DMP 生成的参考位置。`Switch3` 还受 `ref_q_max` 影响，当前 `ref_q_max=0`。 |
| `v` | `TorqueController/dq_ref` | DMP 生成的参考速度。 |
| `PlaybackPhi` | 当前顶层无明显去向 | DMP 播放相位，建议作为监控信号观察轨迹播放进度。 |

### 7.7 TorqueController 与 Torque_Guard 力矩链路

| 信号 | 来源 | 去向/作用 |
|---|---|---|
| `q_meas` | `FootSwitch/ActuralPosition` | 与 `q_ref` 做位置误差，经过 `MO_Kp`。 |
| `dq_meas` | `FootSwitch/ActuralVelocity` | 与 `dq_ref` 做速度误差，经过 `MO_Kd`。 |
| `q_ref` | DMP `y` 经 `Switch3` 后的 `y_limited` | 目标位置。 |
| `dq_ref` | DMP `v` | 目标速度。 |
| `tau_e` | `TorqueController/TorqueManager` | PD 控制与活动/步数 ramp 后的控制力矩。 |
| `MO_DMPPhase0Event` | `TorqueController/Subsystem2` | 送 `TorqueManager`、步数计数、峰值判断；建议监控。 |
| `MO_currentgain` | `TorqueManager` | 当前力矩渐入倍率；建议监控。 |
| `MO_GiveTorque?` 输出 | 顶层力矩开关 | 送入 `Torque_Guard/tau_e`，可切换真实力矩或 0。 |
| `MinimumTauGate` 输出 | `tau_e`、`MO_HealthLegdefault`、`isStanding` 综合 | 根据站立/接触状态在真实力矩和默认健康腿力矩间切换。 |
| `LimitProtect` 输出 | 左右膝位置、腿侧、SafeTorque、力矩输入综合 | 产生安全后的 `Right`、`Left` 力矩。 |
| `Right` | `Torque_Guard` 输出 1 | 经 `MO_RightCurrentAmplifyGain` 和顶层 `Sum1/Saturation` 进入输出总线。 |
| `Left` | `Torque_Guard` 输出 2 | 经顶层 `Sum2/Saturation1` 进入输出总线。 |
