---
paper_id: fed439bb5ce1
title: ANFIS to estimate damping coefficient from EMG to optimize the interaction force
year: 2016
doi: 10.1109/microcom.2016.7522589
pdf_status: open_access_pdf
---

# Evidence Card

## Title
ANFIS to estimate damping coefficient from EMG to optimize the interaction force

## Year
2016

## DOI
10.1109/microcom.2016.7522589

## Abstract
Although Lower Limb Robotic Rehabilitation device exhibit a great prospect in the rehabilitation of impaired limb, yet it has not been widely applied to clinical rehabilitation. This is mostly due to the insufficient bidirectional information interaction between exoskeleton and patient. In the shared control at the interaction point, it is very important that the deficiency of impaired lower limb in sharing the knee joint dynamics (Capturing of the intended action of the patient) is extracted beforehand to estimate as to how much assistance the robotic exoskeleton would provide. The intended action data that can be extracted from EMG signal may include the intended posture, intended torque, intended knee joint angle, intended knee joint torque and impedance parameter. In this paper, an application of Adaptive Network Based Fuzzy Inference System (ANFIS) has been proposed for proprioceptive feedback on the status of the interaction force at the patient robotic exoskeleton interaction point. ANFIS has been used to model the relationship between input and output. Interaction forces, rate of change in surface electromyography (EMG) signal are two inputs to ANFIS model and impedance parameters damping coefficients (also stiffness) is output. Impedance control law has damping as one of the tuning parameter. The resultant total torque is calculated from this law. The proposed model is able to estimate damping and demonstrate decent accuracy in modulating the knee joint dynamics to minimize the interaction force at the Patient Exoskeleton interaction point.

## Keywords
not available in metadata

## Tracked Keywords Found
impedance, exoskeleton, knee, stroke

## System Signals / Parameters Found
q

## introduction_relevant_5
No high-relevance paragraph found by local keyword screening.

## method_relevant_8
1. Ubeyli, “Adaptive neuro-fuzzy inference system for classification of EEG signals using wavelet coefficients,” Journal of neuroscience methods, vol. 148, pp.1130121, 2005. [4] P. Parker, K. Englehart, and B. Hudgins, “Myoelectric signal processing for control of powered limb prostheses, “Journal of electromyography and kinesiology, vol. 16, pp.541-548, 2006. [5] E. D. Ubeyli, “Adaptive neuro-fuzzy interface system for classification of ECG signals using Lyapunov exponents,” Computer methods and programs in biomedicine, vol. 93, pp. 313-321, 2009. [6] J. Hu, Z-G. Hou, L. Peng, and N. Gu, “sEMG-Based Single-Joint Active Training with iLeg-A Horizontal Exoskeleton for Lower Limb Rehabilitation,” in Neural Information Processing, 2004, pp.535-542. [7] T. Takagi and M. Sugeno, “Fuzzy identification of systems and its applications to modeling and control,” Systems, Man and Cybernetics, IEEE Transactions on, pp.116-132, 1985.

## experiment_evaluation_relevant_8
1. When ෤ 0 , the contraction of vastus lateralis muscle (extensor muscle) plays the dominant role. As a result, the knee performs an extension. When0 , the knee performs a flexion since bicep femoris muscle contracts while vastus lateralis muscle relaxes. When෤ଶ =0 , both the extensor and flexor muscles are in relaxation, and consequently the knee maintains still. So ܤ ௜ of the knee joint will very for high variation into the sEMG differences with respect to time. Stiffness of the exoskeleton will be inversely proportional to EMG differences of flexion and extension muscles. VII. I SSUS THAT DETECTS FUZZY RULES AND METHODOLOGY There are two sets of information provided into the Fuzzy inference system that is embedded into the Neural Network of a hybrid ANFIS model. Thes e are respectively interaction force, changes in difference of EMG signal between flexor and extensor. There are two direction of the actuator due to flexion and extension.
2. By our convention, the direction of flexion is clockwise and the direction of extension is anti clockwise. In either way the difference between the EMG of flexion and EMG of extensi on will increase because the flexion-extension muscle works pretty much like on-off fashion. But by the above convention the increase during flexion is considered positive increase and opposite otherwise (negative increase). The natu re of increase in EMG may differ due to the type of postures we are dealing with. In this paper we are concerned with difference in two EMG signals of flexor and extensor muscle because this difference defines the nature of damping. Damping is that phenomena that signifies the amount of energy that is being drained out from the actuator control signal. Low damping means high joint torques and high damping means low joint torques. In case of higher degree of difference between EMG signals of flexion and extension muscles, lower degree of damping is desired.
3. Figure 7. EMG signal difference of (a) six cycles, (b) during flexion and (c) during extension movement. TABLE I. RULE DATABASE OF FUZZY CONTROLLER Fuzzy Inference Model Antecedent rule of interaction force Antecedent rule of rate of sEMG signal Consequence rule of impedance (damping or stiffness) If Interaction Force is Low If sEMG rate is Low 3.5 If Interaction Force is Medium If sEMG rate is Medium 2.5 If Interaction Force is High If sEMG rate is High 1.5
4. Figure 8. Three dimensional surface plot of effect of Interaction force(∆F) and rate of EMG (∆E) to output(stiffness) So a different degrees of freedom tunnel is ensured for smooth human machine interaction. With low impedance higher degree of deviation and with high impedance low deviation is expected
5. VIII. DATA ANALYSIS ANFIS is trained with data set with a data set of 298x3 with two input vector of interaction force and rate of EMG signal features and one output vector of damping coefficient. The range of interaction is from 0.0025 N-m to 0.0085 N-m. The range of EMG is from 0 to 12000. Only RMS feature of EMG vector is used to generate EMG patterns for ANFIS. The range of damping coefficien t is from 0 to 4. The input vectors are input to Gaussi an Membership Function and output vector is taken from linear Membership Function. ANFIS is trained with data set and performance of ANFIS as estimator of damping coefficient is optimized through back propagation through tuning of C,ߪof Gaussian membership function and tuning of P, Q, r of output linear membership function. Figure 9 shows interesting result of the performance where estimated damping coeffi cient (Red co lor) follows closely the desired damping coefficient (Green color). IX.
6. C ONCLUSION A model was desired to learn or capture the EMG damping pattern of different subjects with different severity levels of stroke, EMG patterns at different phase of rehabilitation or EMG patterns of different age groups and make intelligent decisions at the same time as to how much damping is ideal for the robot rehabilitation device in the shared controlled system. Proposed ANFIS model have served the purpose. A CKNOWLEDGMENT I acknowledge the contribution of my supervisor professor Adel Al Jumaily. REFERENCES [1] Y.H. Yin, Y.J.Fan, and L.D.Xu, “ EMG and ERP-integrated humanmachine interface between the paralyzed and rehabilitation exoskeleton,” Information Technology in Biomedicine, IEEE Transaction on, vol. 16,pp. 542-549,2012 [2] S. N. i. Sidek and A. J. H. Mohideen, “ Mapping of EMG signal to hand grip force at varying wrist angles,” in Biomedical Engineering and Sciences (IECBES), 2012 IEEE EMBS Conference on, 2012,pp. 648-653. [3] I. Guler and E. D.

## conclusion_relevant_5
No high-relevance paragraph found by local keyword screening.
