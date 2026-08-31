#ifndef RTW_HEADER_slrt_filelog_minimal_cal_h_
#define RTW_HEADER_slrt_filelog_minimal_cal_h_
#include "rtwtypes.h"

/* Storage class 'PageSwitching', for system '<Root>' */
struct slrt_filelog_minimal_cal_type {
  real_T sine_source_Amp;              /* Expression: 1
                                        * Referenced by: '<Root>/sine_source'
                                        */
  real_T sine_source_Bias;             /* Expression: 0
                                        * Referenced by: '<Root>/sine_source'
                                        */
  real_T sine_source_Freq;             /* Expression: 2*pi*1
                                        * Referenced by: '<Root>/sine_source'
                                        */
  real_T sine_source_Hsin;             /* Computed Parameter: sine_source_Hsin
                                        * Referenced by: '<Root>/sine_source'
                                        */
  real_T sine_source_HCos;             /* Computed Parameter: sine_source_HCos
                                        * Referenced by: '<Root>/sine_source'
                                        */
  real_T sine_source_PSin;             /* Computed Parameter: sine_source_PSin
                                        * Referenced by: '<Root>/sine_source'
                                        */
  real_T sine_source_PCos;             /* Computed Parameter: sine_source_PCos
                                        * Referenced by: '<Root>/sine_source'
                                        */
  boolean_T file_log_enable_Value;     /* Expression: true
                                        * Referenced by: '<Root>/file_log_enable'
                                        */
};

/* Storage class 'PageSwitching' */
extern slrt_filelog_minimal_cal_type slrt_filelog_minimal_cal_impl;
extern slrt_filelog_minimal_cal_type *slrt_filelog_minimal_cal;

#endif                              /* RTW_HEADER_slrt_filelog_minimal_cal_h_ */
