#ifndef RTW_HEADER_slrt_mat_playback_cal_h_
#define RTW_HEADER_slrt_mat_playback_cal_h_
#include "rtwtypes.h"

/* Storage class 'PageSwitching', for system '<Root>' */
struct slrt_mat_playback_cal_type {
  boolean_T file_log_enable_Value;     /* Expression: true
                                        * Referenced by: '<Root>/file_log_enable'
                                        */
};

/* Storage class 'PageSwitching' */
extern slrt_mat_playback_cal_type slrt_mat_playback_cal_impl;
extern slrt_mat_playback_cal_type *slrt_mat_playback_cal;

#endif                                 /* RTW_HEADER_slrt_mat_playback_cal_h_ */
