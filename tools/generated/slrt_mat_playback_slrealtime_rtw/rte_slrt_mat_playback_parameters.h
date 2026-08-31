#ifndef _RTE_SLRT_MAT_PLAYBACK_PARAMETERS_H
#define _RTE_SLRT_MAT_PLAYBACK_PARAMETERS_H
#include "rtwtypes.h"
#include "SegmentInfo.hpp"
#include "multiword_types.h"
#include "slrt_mat_playback_types.h"

struct RTE_Param_Service_T {
  real_T replay_left_torque_bp[12001];
  real_T replay_left_torque_data[12001];
  real_T replay_phi_bp[12001];
  real_T replay_phi_data[12001];
  real_T replay_right_torque_bp[12001];
  real_T replay_right_torque_data[12001];
};

extern RTE_Param_Service_T RTE_Param_Service;
extern RTE_Param_Service_T *RTE_Param_Service_ptr;
real_T* get_replay_left_torque_bp(void);
real_T* get_replay_left_torque_data(void);
real_T* get_replay_phi_bp(void);
real_T* get_replay_phi_data(void);
real_T* get_replay_right_torque_bp(void);
real_T* get_replay_right_torque_data(void);
namespace slrealtime
{
  SegmentVector &getSegmentVector(void);
}                                      // slrealtime

#endif
