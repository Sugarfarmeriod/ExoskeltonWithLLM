# Top 10 Must Read

> 范围说明：本研究计划使用 8 名健康受试者，系统实现不使用 EMG 或 IMU。清单中的 EMG/IMU 相关论文仅用于学习 HIL/优化方法，不能作为本研究传感器、目标函数或实验流程的直接模板。

1. **A Two-Layer Human-in-the-Loop Optimization Framework for Customizing Lower-Limb Exoskeleton Assistance** (2023) - score 115
   - AI 插入位置：参数优化器
   - 控制/优化：助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板
   - DOI：10.36227/techrxiv.22327378.v1

2. **A Lower Limb Exoskeleton Adaptive Control Method Based on Model-free Reinforcement Learning and Improved Dynamic Movement Primitives** (2025) - score 106
   - AI 插入位置：参数优化器
   - 控制/优化：助力时机/phase_offset, MO_Kp/MO_Kd/阻抗参数
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset
   - DOI：10.1007/s10846-025-02230-7

3. **Human-in-the-loop Optimisation in Robot-assisted Gait Training** (2025) - score 99
   - AI 插入位置：参数优化器
   - 控制/优化：助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器
   - DOI：10.48550/arxiv.2510.05780

4. **Comparing optimized exoskeleton assistance of the hip, knee, and ankle in single and multi-joint configurations** (2021) - score 96
   - AI 插入位置：参数优化器
   - 控制/优化：助力强度/Amplitude/torque profile
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板
   - DOI：10.1017/wtc.2021.14

5. **On human-in-the-loop optimization of human–robot interaction** (2024) - score 95
   - AI 插入位置：参数优化器
   - 控制/优化：助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束
   - DOI：10.1038/s41586-024-07697-2

6. **Reducing the muscle activity of walking using a portable hip exoskeleton based on human-in-the-loop optimization** (2023) - score 95
   - AI 插入位置：参数优化器
   - 控制/优化：助力强度/Amplitude/torque profile
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束
   - DOI：10.3389/fbioe.2023.1006326

7. **Review of adaptive control for stroke lower limb exoskeleton rehabilitation robot based on motion intention recognition** (2023) - score 94
   - AI 插入位置：状态估计器
   - 控制/优化：助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数
   - 为什么优先：可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束
   - DOI：10.3389/fnbot.2023.1186175

8. **Shaping high-performance wearable robots for human motor and sensory reconstruction and enhancement** (2024) - score 91
   - AI 插入位置：参数优化器
   - 控制/优化：MO_Kp/MO_Kd/阻抗参数
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd
   - DOI：10.1038/s41467-024-46249-0

9. **Optimization of Torque-Control Model for Quasi-Direct-Drive Knee Exoskeleton Robots Based on Regression Forecasting** (2024) - score 87
   - AI 插入位置：参数优化器
   - 控制/优化：MO_Kp/MO_Kd/阻抗参数
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板
   - DOI：10.3390/s24051505

10. **Reducing Squat Physical Effort Using Personalized Assistance From an Ankle Exoskeleton** (2022) - score 84
   - AI 插入位置：参数优化器
   - 控制/优化：助力强度/Amplitude/torque profile
   - 为什么优先：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束
   - DOI：10.1109/tnsre.2022.3186692
