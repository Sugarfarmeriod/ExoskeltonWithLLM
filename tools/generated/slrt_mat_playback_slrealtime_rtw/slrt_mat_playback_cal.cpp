#include "slrt_mat_playback_cal.h"
#include "slrt_mat_playback.h"

/* Storage class 'PageSwitching' */
slrt_mat_playback_cal_type slrt_mat_playback_cal_impl = {
  true
};

slrt_mat_playback_cal_type *slrt_mat_playback_cal = &slrt_mat_playback_cal_impl;
