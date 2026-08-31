# Introduction

卒中是导致死亡和长期残疾负担的重要疾病之一，许多幸存者会遗留不同程度的下肢运动功能障碍[1]–[3]。重复、足量且具有任务针对性的训练有助于改善神经损伤后的运动功能[4]，下肢外骨骼因而被用于提供可重复、可控的关节运动引导和步行辅助[5]。现有外骨骼既可为严重运动障碍者提供完整运动引导，也可为保留主动运动能力者提供部分助力[6]。对于后者，如何根据人体运动状态调节助力时机和强度，是实现协调辅助需要解决的问题。

围绕助力与人体运动的协调，Lora-Millán等[7]利用健侧运动实现患侧装置的同步辅助，Huang等[8]则在轻量准直驱膝关节外骨骼上实现了连续力矩控制。然而，穿戴者之间的步态、关节活动范围和助力偏好存在差异，同一穿戴者的运动状态也会随行走速度、任务和适应过程发生变化。为此，Chen等[9]将动态运动基元、贝叶斯优化和可变阻抗控制结合，用于不同穿戴者和多种任务的辅助；Slade等[10]利用自然行走数据搜索个体化踝关节助力；Wang等[11]针对膝关节屈曲辅助设计了人机在环优化流程。此类方法能够在预先规定的目标、评价指标和参数空间内寻找较优方案，但优化结果仍受到人体适应时间和验证方式的影响，参数收敛也不必然带来实际性能改善[12]。

事实上，外骨骼适配并不只是给定目标下的参数搜索。Slade等[13]指出，人机在环优化需要综合考虑控制参数化、人体响应测量、优化目标、算法选择与实验流程，同时还会受到测量噪声和人体适应的影响。Welker等[14]在踝足假肢模拟器实验中观察到，优化所得控制器并未稳定带来代谢率改善或明确的使用者偏好，说明优化目标与实际适配效果之间可能存在差异。基于上述问题，本文进一步考虑数据质量不足、穿戴者反馈与客观测量不一致以及训练目标变化等情形。在这些情形下，系统需要在保持当前方案、重新分析、请求补充信息、有界调整、拒绝更新或停止调节等预定动作之间作出选择。本文将这一过程定义为实验轮次之间的适配决策，以区别于既定目标和参数空间内的数值优化。

实验轮次之间的适配仍需建立在确定性的实时控制基础上。动态运动基元能够以少量参数描述和调节参考运动，并已用于运动生成、轨迹调制和物理交互[15]。本团队前期研制了准直驱膝关节外骨骼，将在线增量动态运动基元与阻抗控制结合，为参考轨迹调整和柔顺助力提供了硬件与控制基础[16]；Shushtari等[17]研究了连续步态相位估计，Zhou等[18]将动态运动基元调制用于下肢康复机器人的柔顺控制，为相位信息获取、参考运动生成与柔顺执行的模块化设计提供了技术参考。本文将由若干完整步态周期构成的数据窗口作为一次适配轮次的观测单元；窗口内由实时控制器承担连续运动执行，状态评价与参数调整则在相邻轮次之间由独立的低频决策层完成。

大语言模型为上述轮次间决策提供了新的实现途径。Huang等[19]和Liang等[20]将环境状态、执行结果和人工反馈纳入语言模型规划，使机器人能够在任务失败后修正后续步骤；Liang等[21]通过预定义接口连接语言模型与机器人能力，Ichter等[22]则利用技能可执行性限制高层动作选择。在外骨骼与康复机器人中，Chen等[23]、von Waldow等[24]和Chen等[25]分别探索了命令扩展、治疗意图到参数的转换以及语义规划与底层控制的分离。这些研究表明，大语言模型可用于语言理解、工具选择和高层方案组织；考虑到人体外骨骼对实时性、确定性和安全性的要求，本文将其作用限制在实验轮次之间的决策层，而不直接参与连续实时控制。

要将这种能力用于膝关节外骨骼，还需要同时处理三个层面的问题：在信息层，穿戴者语言反馈和变化的实验目标需要与客观实验数据建立联系；在决策层，系统需要在数据异常、反馈冲突和目标变化时选择相应的分析与调节策略；在执行层，大语言模型的输出必须受到确定性工具、参数边界和独立安全裁决的限制[24]–[26]，并经实验人员确认后才能用于下一轮实验。现有研究多分别处理其中某一层面，面向膝关节外骨骼进行统一设计与验证的研究仍较少。

针对上述问题，本文在前期准直驱膝关节外骨骼及在线增量动态运动基元控制基础[16]上，引入按实验轮次低频工作的受约束大语言模型智能体。本文的主要贡献体现在以下三个方面：1）提出一种面向膝关节外骨骼的轮次间交互式适配架构，明确大语言模型智能体、确定性分析工具、实时控制器、独立安全约束和人工确认之间的功能边界；2）建立穿戴者语言反馈与客观评价指标之间的关联机制，使智能体能够根据反馈类别选择相应的实验数据分析工具，并将主观需求与客观结果共同用于状态评价；3）提出面向在线增量动态运动基元控制的轮次间参数决策机制，在数据异常、反馈冲突或目标变化时，从保持、重新分析、拒绝更新和有界调整等预定动作中形成下一轮方案，并对参考运动幅值、相位偏移和阻抗增益等候选参数进行边界检查。本文在健康受试者行走实验中，将智能体接入实时控制环之外的轮次间在线适配流程，检验其能否依据已完成步态窗口的数据形成经安全检查和人工确认的下一轮参数方案，以及目标指标是否按预期变化。

本文其余部分安排如下：第2节介绍准直驱膝关节外骨骼的系统组成及实时控制基础；第3节给出受约束大语言模型智能体的适配方法、评价工具、参数决策过程和安全约束；第4节介绍离线情景测试与基于步态窗口的健康受试者轮次间在线适配实验及其评价指标；第5节分析实验结果，总结本文工作，并讨论方法局限与后续研究方向。

## 参考文献

[1] V. L. Feigin et al., “World Stroke Organization: Global Stroke Fact Sheet 2025,” *International Journal of Stroke*, vol. 20, no. 2, pp. 132–144, 2025.

[2] D. R. Louie, L. A. Simpson, W. B. Mortenson, et al., “Prevalence of Walking Limitation After Acute Stroke and Its Impact on Discharge to Home,” *Physical Therapy*, vol. 102, no. 1, p. pzab246, 2022.

[3] C. Beyaert, R. Vasa, and G. E. Frykberg, “Gait Post-Stroke: Pathophysiology and Rehabilitation Strategies,” *Neurophysiologie Clinique/Clinical Neurophysiology*, vol. 45, no. 4–5, pp. 335–355, 2015.

[4] T. G. Hornby et al., “Clinical Practice Guideline to Improve Locomotor Function Following Chronic Stroke, Incomplete Spinal Cord Injury, and Brain Injury,” *Journal of Neurologic Physical Therapy*, vol. 44, no. 1, pp. 49–100, 2020.

[5] V. Warutkar, R. Dadgal, and U. R. Mangulkar, “Use of Robotics in Gait Rehabilitation Following Stroke: A Review,” *Cureus*, vol. 14, no. 11, p. e31075, 2022.

[6] R. Baud, A. R. Manzoori, A. Ijspeert, and M. Bouri, “Review of Control Strategies for Lower-Limb Exoskeletons to Assist Gait,” *Journal of NeuroEngineering and Rehabilitation*, 2021. DOI: 10.1186/s12984-021-00906-3.

[7] J. S. Lora-Millán et al., “A Unilateral Robotic Knee Exoskeleton to Assess the Role of Natural Gait Assistance in Hemiparetic Patients,” *Journal of NeuroEngineering and Rehabilitation*, 2022. DOI: 10.1186/s12984-022-01088-2.

[8] T.-H. Huang et al., “Modeling and Stiffness-Based Continuous Torque Control of Lightweight Quasi-Direct-Drive Knee Exoskeletons for Versatile Walking Assistance,” *IEEE Transactions on Robotics*, 2022. DOI: 10.1109/TRO.2022.3170287.

[9] Y. Chen et al., “Learning to Assist Different Wearers in Multitasks: Efficient and Individualized Human-in-the-Loop Adaptation Framework for Lower-Limb Exoskeleton,” *IEEE Transactions on Robotics*, 2024. DOI: 10.1109/TRO.2024.3468768.

[10] P. Slade et al., “Personalizing Exoskeleton Assistance While Walking in the Real World,” *Nature*, 2022. DOI: 10.1038/s41586-022-05191-1.

[11] Z. Wang et al., “Human-in-the-Loop Optimization for Knee Exoskeleton Flexion Assistance,” *IEEE Robotics and Automation Letters*, 2025. DOI: 10.1109/LRA.2025.3526558.

[12] A. Christou, A. Sochopoulos, E. Lister, and S. Vijayakumar, “Human-in-the-Loop Optimisation in Robot-Assisted Gait Training,” arXiv preprint, 2025. DOI: 10.48550/arXiv.2510.05780.

[13] P. Slade et al., “On Human-in-the-Loop Optimization of Human–Robot Interaction,” *Nature*, 2024. DOI: 10.1038/s41586-024-07697-2.

[14] C. G. Welker, A. S. Voloshina, V. L. Chiu, and S. H. Collins, “Shortcomings of Human-in-the-Loop Optimization of an Ankle-Foot Prosthesis Emulator: A Case Series,” *Royal Society Open Science*, 2021. DOI: 10.1098/rsos.202020.

[15] M. Saveriano, F. J. Abu-Dakka, A. Kramberger, and L. Peternel, “Dynamic Movement Primitives in Robotics: A Tutorial Survey,” *The International Journal of Robotics Research*, 2023. DOI: 10.1177/02783649231201196.

[16] 朱宇, 王向阳, 孙健铨, 袁博, 马跃, “基于在线增量DMP的准直驱膝关节外骨骼自适应柔顺控制,” *仪器仪表学报*, 网络首发, 2026. DOI: 10.19650/j.cnki.cjsi.J2614961.

[17] M. Shushtari et al., “Ultra-Robust Real-Time Estimation of Gait Phase,” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 2022. DOI: 10.1109/TNSRE.2022.3207919.

[18] J. Zhou et al., “Dynamic Movement Primitives Modulation-Based Compliance Control for a New Sitting/Lying Lower Limb Rehabilitation Robot,” *IEEE Access*, 2024. DOI: 10.1109/ACCESS.2024.3376391.

[19] W. Huang et al., “Inner Monologue: Embodied Reasoning through Planning with Language Models,” in *Proceedings of the 6th Conference on Robot Learning*, PMLR, vol. 205, pp. 1769–1782, 2023.

[20] J. Liang et al., “Learning to Learn Faster from Human Feedback with Language Model Predictive Control,” in *Proceedings of Robotics: Science and Systems XX*, 2024. DOI: 10.15607/RSS.2024.XX.125.

[21] J. Liang et al., “Code as Policies: Language Model Programs for Embodied Control,” in *Proceedings of the IEEE International Conference on Robotics and Automation*, 2023. DOI: 10.1109/ICRA48891.2023.10160591.

[22] B. Ichter et al., “Do As I Can, Not As I Say: Grounding Language in Robotic Affordances,” in *Proceedings of the 6th Conference on Robot Learning*, PMLR, vol. 205, pp. 287–318, 2023.

[23] W. Chen et al., “LLM-Enabled Incremental Learning Framework for Hand Exoskeleton Control,” *IEEE Transactions on Automation Science and Engineering*, vol. 22, pp. 2617–2626, 2025. DOI: 10.1109/TASE.2024.3382679.

[24] M.-O. von Waldow et al., “Virtual Technician: A Multi-Modal Interface Facilitating Therapists’ Adoption of Rehab Robots,” *Proceedings on Automation in Medical Engineering*, vol. 3, no. 1, Art. no. 2512, 2026. DOI: 10.18416/AUTOMED.2026.2512.

[25] Y. Chen et al., “A Semantic-Aware Framework for Safe and Intent-Integrative Assistance in Upper-Limb Exoskeletons,” *IEEE Robotics and Automation Letters*, vol. 11, no. 5, pp. 5938–5945, 2026. DOI: 10.1109/LRA.2026.3677710.

[26] Z. Yang, S. S. Raman, A. Shah, and S. Tellex, “Plug in the Safety Chip: Enforcing Constraints for LLM-Driven Robot Agents,” in *Proceedings of the 2024 IEEE International Conference on Robotics and Automation*, pp. 14435–14442, 2024. DOI: 10.1109/ICRA57147.2024.10611447.
