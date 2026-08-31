#include "slrt_filelog_smoke_cal.h"
#include "slrt_filelog_smoke.h"

/* Storage class 'PageSwitching' */
slrt_filelog_smoke_cal_type slrt_filelog_smoke_cal_impl = {
  /* Expression: 42
   * Referenced by: '<Root>/smoke_constant_source'
   */
  42.0,

  /* Computed Parameter: smoke_counter_integrator_gainva
   * Referenced by: '<Root>/smoke_counter_integrator'
   */
  1.0E-6,

  /* Expression: 0
   * Referenced by: '<Root>/smoke_counter_integrator'
   */
  0.0,

  /* Expression: 1
   * Referenced by: '<Root>/counter_increment_source'
   */
  1.0,

  /* Expression: 1
   * Referenced by: '<Root>/smoke_sine_source'
   */
  1.0,

  /* Expression: 0
   * Referenced by: '<Root>/smoke_sine_source'
   */
  0.0,

  /* Expression: 2*pi*1
   * Referenced by: '<Root>/smoke_sine_source'
   */
  6.2831853071795862,

  /* Computed Parameter: smoke_sine_source_Hsin
   * Referenced by: '<Root>/smoke_sine_source'
   */
  0.0062831439655589511,

  /* Computed Parameter: smoke_sine_source_HCos
   * Referenced by: '<Root>/smoke_sine_source'
   */
  0.99998026085613712,

  /* Computed Parameter: smoke_sine_source_PSin
   * Referenced by: '<Root>/smoke_sine_source'
   */
  -0.0062831439655589511,

  /* Computed Parameter: smoke_sine_source_PCos
   * Referenced by: '<Root>/smoke_sine_source'
   */
  0.99998026085613712
};

slrt_filelog_smoke_cal_type *slrt_filelog_smoke_cal =
  &slrt_filelog_smoke_cal_impl;
