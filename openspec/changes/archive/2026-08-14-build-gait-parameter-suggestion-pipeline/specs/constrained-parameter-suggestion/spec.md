## ADDED Requirements

### Requirement: 有边界的建议空间
系统 SHALL 将参数建议限制在预定义的有边界动作空间内。

#### Scenario: 生成建议
- **WHEN** 指标和可靠性检查支持给出建议
- **THEN** 系统只为允许的参数输出保持、轻微增大、轻微减小、轻微提前或轻微延后动作

#### Scenario: 请求不支持的参数
- **WHEN** 规则或调用方请求为允许集合之外的参数生成建议
- **THEN** 系统拒绝该建议，并记录不支持的参数名

### Requirement: 相位偏移规则
系统 SHALL 仅在相位指标可靠且超过配置阈值时，建议修改 `phase_offset`。

#### Scenario: 患侧相位偏晚
- **WHEN** 相位可靠性可接受，且相位延迟超过偏晚阈值
- **THEN** 系统建议 `phase_offset` 轻微提前

#### Scenario: 相位可靠性低
- **WHEN** 相位可靠性低，或无法计算相位延迟
- **THEN** 系统 SHALL NOT 建议修改 `phase_offset`

### Requirement: 幅值与助力规则
系统 SHALL 仅在运动误差和力矩余量支持调整时，建议修改幅值或助力。

#### Scenario: 峰值屈曲不足且力矩有余量
- **WHEN** 患侧峰值屈曲低于参考且超过配置阈值，并且力矩限幅比例低于安全否决阈值
- **THEN** 系统建议 `Amplitude` 或助力增益轻微增大

#### Scenario: 力矩接近安全限幅
- **WHEN** 力矩限幅比例超过安全否决阈值，或 Torque_Guard 触发过多
- **THEN** 系统 SHALL NOT 建议增大 `Amplitude`、助力增益或 `MO_Kp`

### Requirement: 阻抗增益规则
系统 SHALL 仅在跟踪指标、力矩余量和数据质量可接受时，建议修改 `MO_Kp` 或 `MO_Kd`。

#### Scenario: 跟踪误差大且力矩有余量
- **WHEN** tracking RMSE 超过配置阈值，数据质量可用，并且力矩余量可接受
- **THEN** 系统可以建议 `MO_Kp` 轻微增大，或给出保守的助力相关调整

#### Scenario: 跟踪误差大但接近力矩限幅
- **WHEN** tracking RMSE 较大，但力矩限幅比例超过安全否决阈值
- **THEN** 系统不建议增加增益，并记录受安全限制的理由

### Requirement: 建议可追溯性
系统 SHALL 在每条建议中包含所使用的指标、阈值和规则标识。

#### Scenario: 生成推荐
- **WHEN** 系统写出 `parameter_suggestion.json`
- **THEN** 每条推荐包含参数名、动作、理由、来源指标、阈值、否决检查和置信度或可靠性等级

#### Scenario: 没有安全建议
- **WHEN** 所有候选建议都被数据质量或安全约束否决
- **THEN** 系统写出保守的保持不变结果，并列出否决原因
