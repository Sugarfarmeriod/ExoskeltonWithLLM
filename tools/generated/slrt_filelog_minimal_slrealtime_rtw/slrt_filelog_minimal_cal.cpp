#include "slrt_filelog_minimal_cal.h"
#include "slrt_filelog_minimal.h"

/* Storage class 'PageSwitching' */
slrt_filelog_minimal_cal_type slrt_filelog_minimal_cal_impl = {
  /* Expression: 1
   * Referenced by: '<Root>/sine_source'
   */
  1.0,

  /* Expression: 0
   * Referenced by: '<Root>/sine_source'
   */
  0.0,

  /* Expression: 2*pi*1
   * Referenced by: '<Root>/sine_source'
   */
  6.2831853071795862,

  /* Computed Parameter: sine_source_Hsin
   * Referenced by: '<Root>/sine_source'
   */
  0.0062831439655589511,

  /* Computed Parameter: sine_source_HCos
   * Referenced by: '<Root>/sine_source'
   */
  0.99998026085613712,

  /* Computed Parameter: sine_source_PSin
   * Referenced by: '<Root>/sine_source'
   */
  -0.0062831439655589511,

  /* Computed Parameter: sine_source_PCos
   * Referenced by: '<Root>/sine_source'
   */
  0.99998026085613712,

  /* Expression: true
   * Referenced by: '<Root>/file_log_enable'
   */
  true
};

slrt_filelog_minimal_cal_type *slrt_filelog_minimal_cal =
  &slrt_filelog_minimal_cal_impl;
