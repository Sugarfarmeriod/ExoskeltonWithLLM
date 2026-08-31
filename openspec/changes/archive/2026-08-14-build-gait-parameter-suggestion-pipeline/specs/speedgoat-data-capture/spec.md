## ADDED Requirements

### Requirement: 记录信号清单
系统 SHALL 定义一份 Speedgoat 试次记录信号清单，覆盖后续步态分析和参数建议所需的最小信号集合。

#### Scenario: 配置记录信号
- **WHEN** 工程师准备一次直线行走试验
- **THEN** 系统记录 `q_meas`、`dq_meas`、`q_ref`、`dq_ref`、`FeetLoad`、`Phi`、`Phase0Event`、`tau_e`、`SafeTorque`、助力使能状态和关键控制参数

#### Scenario: 信号缺少可追溯名称
- **WHEN** 某个记录信号没有稳定名称或路径
- **THEN** 系统要求先补充信号命名或映射表，再允许进入正式采集流程

### Requirement: 目标机文件日志采集
系统 SHALL 优先使用 Simulink Real-Time 支持的目标机文件日志机制采集试次数据。

#### Scenario: 使用现有 SLRT Explorer 工作流
- **WHEN** 工程师按照现有流程通过 Ctrl+B 编译 `.mldatx`，并在 SLRT Explorer 中上传和运行应用
- **THEN** 数据采集流程 SHALL 与该人工部署和调参流程兼容，不要求脚本自动部署或启动外骨骼工程模型

#### Scenario: 试次开始
- **WHEN** 模型已部署到 Speedgoat，且目标机连接正常
- **THEN** 工程师可以启动应用并开始一次带 trial_id 的数据记录

#### Scenario: 试次结束
- **WHEN** 行走试次结束或人工停止助力
- **THEN** 系统停止记录并保留目标机上的本次试次日志

### Requirement: 日志下载与归档
系统 SHALL 将 Speedgoat 目标机日志下载到本地项目目录，并保留试次元数据。

#### Scenario: 下载成功
- **WHEN** 目标机存在本次试次日志
- **THEN** 系统将日志下载到本地 `data/raw/<trial_id>/` 或等价目录，并写入采集时间、模型名、采样时间、受试者或匿名编号、患侧和参数快照

#### Scenario: 下载失败
- **WHEN** 目标机连接失败、日志不存在或文件损坏
- **THEN** 系统记录失败原因，并且不生成后续分析输入

#### Scenario: 参数在 SLRT Explorer 中修改
- **WHEN** 工程师在 SLRT Explorer 中修改运行参数
- **THEN** 归档元数据 SHALL 记录本次试次使用的参数快照或要求工程师提供参数快照文件

### Requirement: 分析输入导出
系统 SHALL 将下载的日志转换为后续 Python 分析可读取的规范文件。

#### Scenario: 导出成功
- **WHEN** 目标机日志已下载并能被 MATLAB/Simulink Real-Time 读取
- **THEN** 系统导出 CSV 或 MAT 文件，字段名遵循规范试次输入 schema

#### Scenario: 采样率或长度不一致
- **WHEN** 不同信号采样率、时间戳或长度不一致
- **THEN** 系统在导出时保留时间向量，并标记需要重采样或对齐的信号
