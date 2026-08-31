#include "rte_slrt_filelog_smoke_parameters.h"
#include "slrt_filelog_smoke.h"
#include "slrt_filelog_smoke_cal.h"

extern slrt_filelog_smoke_cal_type slrt_filelog_smoke_cal_impl;
namespace slrealtime
{
  /* Description of SEGMENTS */
  SegmentVector segmentInfo {
    { (void*)&slrt_filelog_smoke_cal_impl, (void**)&slrt_filelog_smoke_cal,
      sizeof(slrt_filelog_smoke_cal_type), 2 }
  };

  SegmentVector &getSegmentVector(void)
  {
    return segmentInfo;
  }
}                                      // slrealtime
