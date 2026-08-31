#ifndef RTW_HEADER_slrt_filelog_smoke_cal_h_
#define RTW_HEADER_slrt_filelog_smoke_cal_h_
#include "rtwtypes.h"

/* Storage class 'PageSwitching', for system '<Root>' */
struct slrt_filelog_smoke_cal_type {
  real_T smoke_constant_source_Value;  /* Expression: 42
                                        * Referenced by: '<Root>/smoke_constant_source'
                                        */
  real_T smoke_counter_integrator_gainva;
                          /* Computed Parameter: smoke_counter_integrator_gainva
                           * Referenced by: '<Root>/smoke_counter_integrator'
                           */
  real_T smoke_counter_integrator_IC;  /* Expression: 0
                                        * Referenced by: '<Root>/smoke_counter_integrator'
                                        */
  real_T counter_increment_source_Value;/* Expression: 1
                                         * Referenced by: '<Root>/counter_increment_source'
                                         */
  real_T smoke_sine_source_Amp;        /* Expression: 1
                                        * Referenced by: '<Root>/smoke_sine_source'
                                        */
  real_T smoke_sine_source_Bias;       /* Expression: 0
                                        * Referenced by: '<Root>/smoke_sine_source'
                                        */
  real_T smoke_sine_source_Freq;       /* Expression: 2*pi*1
                                        * Referenced by: '<Root>/smoke_sine_source'
                                        */
  real_T smoke_sine_source_Hsin;   /* Computed Parameter: smoke_sine_source_Hsin
                                    * Referenced by: '<Root>/smoke_sine_source'
                                    */
  real_T smoke_sine_source_HCos;   /* Computed Parameter: smoke_sine_source_HCos
                                    * Referenced by: '<Root>/smoke_sine_source'
                                    */
  real_T smoke_sine_source_PSin;   /* Computed Parameter: smoke_sine_source_PSin
                                    * Referenced by: '<Root>/smoke_sine_source'
                                    */
  real_T smoke_sine_source_PCos;   /* Computed Parameter: smoke_sine_source_PCos
                                    * Referenced by: '<Root>/smoke_sine_source'
                                    */
};

/* Storage class 'PageSwitching' */
extern slrt_filelog_smoke_cal_type slrt_filelog_smoke_cal_impl;
extern slrt_filelog_smoke_cal_type *slrt_filelog_smoke_cal;

#endif                                /* RTW_HEADER_slrt_filelog_smoke_cal_h_ */
