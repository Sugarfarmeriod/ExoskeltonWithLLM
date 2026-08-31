/*
 * slrt_mat_playback.cpp
 *
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * Code generation for model "slrt_mat_playback".
 *
 * Model version              : 1.1
 * Simulink Coder version : 23.2 (R2023b) 01-Aug-2023
 * C++ source code generated on : Mon Jun 29 22:52:37 2026
 *
 * Target selection: slrealtime.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: Intel->x86-64 (Linux 64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "slrt_mat_playback.h"
#include "slrt_mat_playback_cal.h"
#include "rte_slrt_mat_playback_parameters.h"
#include "slrt_mat_playback_private.h"
#include <cstring>

extern "C"
{

#include "rt_nonfinite.h"

}

/* Block signals (default storage) */
B_slrt_mat_playback_T slrt_mat_playback_B;

/* Block states (default storage) */
DW_slrt_mat_playback_T slrt_mat_playback_DW;

/* Real-time model */
RT_MODEL_slrt_mat_playback_T slrt_mat_playback_M_ = RT_MODEL_slrt_mat_playback_T
  ();
RT_MODEL_slrt_mat_playback_T *const slrt_mat_playback_M = &slrt_mat_playback_M_;
real_T look1_binlcpw(real_T u0, const real_T bp0[], const real_T table[],
                     uint32_T maxIndex)
{
  real_T frac;
  real_T yL_0d0;
  uint32_T iLeft;

  /* Column-major Lookup 1-D
     Search method: 'binary'
     Use previous index: 'off'
     Interpolation method: 'Linear point-slope'
     Extrapolation method: 'Clip'
     Use last breakpoint for index at or above upper limit: 'off'
     Remove protection against out-of-range input in generated code: 'off'
   */
  /* Prelookup - Index and Fraction
     Index Search method: 'binary'
     Extrapolation method: 'Clip'
     Use previous index: 'off'
     Use last breakpoint for index at or above upper limit: 'off'
     Remove protection against out-of-range input in generated code: 'off'
   */
  if (u0 <= bp0[0U]) {
    iLeft = 0U;
    frac = 0.0;
  } else if (u0 < bp0[maxIndex]) {
    uint32_T bpIdx;
    uint32_T iRght;

    /* Binary Search */
    bpIdx = maxIndex >> 1U;
    iLeft = 0U;
    iRght = maxIndex;
    while (iRght - iLeft > 1U) {
      if (u0 < bp0[bpIdx]) {
        iRght = bpIdx;
      } else {
        iLeft = bpIdx;
      }

      bpIdx = (iRght + iLeft) >> 1U;
    }

    frac = (u0 - bp0[iLeft]) / (bp0[iLeft + 1U] - bp0[iLeft]);
  } else {
    iLeft = maxIndex - 1U;
    frac = 1.0;
  }

  /* Column-major Interpolation 1-D
     Interpolation method: 'Linear point-slope'
     Use last breakpoint for index at or above upper limit: 'off'
     Overflow mode: 'portable wrapping'
   */
  yL_0d0 = table[iLeft];
  return (table[iLeft + 1U] - yL_0d0) * frac + yL_0d0;
}

/* Model step function */
void slrt_mat_playback_step(void)
{
  /* Clock: '<Root>/clock' */
  slrt_mat_playback_B.clock = slrt_mat_playback_M->Timing.t[0];

  /* Lookup_n-D: '<Root>/replay_left_torque_lookup' incorporates:
   *  Clock: '<Root>/clock'
   */
  slrt_mat_playback_B.replay_left_torque_filelog = look1_binlcpw
    (slrt_mat_playback_B.clock, get_replay_left_torque_bp(),
     get_replay_left_torque_data(), 12000U);

  /* Lookup_n-D: '<Root>/replay_phi_lookup' incorporates:
   *  Clock: '<Root>/clock'
   */
  slrt_mat_playback_B.replay_phi_filelog = look1_binlcpw
    (slrt_mat_playback_B.clock, get_replay_phi_bp(), get_replay_phi_data(),
     12000U);

  /* Lookup_n-D: '<Root>/replay_right_torque_lookup' incorporates:
   *  Clock: '<Root>/clock'
   */
  slrt_mat_playback_B.replay_right_torque_filelog = look1_binlcpw
    (slrt_mat_playback_B.clock, get_replay_right_torque_bp(),
     get_replay_right_torque_data(), 12000U);

  /* ToAsyncQueueBlock generated from: '<S1>/replay_left_torque_lookup' */
  slrtLogSignal
    (slrt_mat_playback_DW.TAQSigLogging_InsertedFor_rep_m.SLRTSigHandles,
     (((slrt_mat_playback_M->Timing.clockTick1+
        slrt_mat_playback_M->Timing.clockTickH1* 4294967296.0)) * 0.001));

  /* ToAsyncQueueBlock generated from: '<S2>/replay_phi_lookup' */
  slrtLogSignal
    (slrt_mat_playback_DW.TAQSigLogging_InsertedFor_rep_c.SLRTSigHandles,
     (((slrt_mat_playback_M->Timing.clockTick1+
        slrt_mat_playback_M->Timing.clockTickH1* 4294967296.0)) * 0.001));

  /* ToAsyncQueueBlock generated from: '<S3>/replay_right_torque_lookup' */
  slrtLogSignal
    (slrt_mat_playback_DW.TAQSigLogging_InsertedFor_rep_k.SLRTSigHandles,
     (((slrt_mat_playback_M->Timing.clockTick1+
        slrt_mat_playback_M->Timing.clockTickH1* 4294967296.0)) * 0.001));

  /* Constant: '<Root>/file_log_enable' */
  slrt_mat_playback_B.file_log_enable =
    slrt_mat_playback_cal->file_log_enable_Value;

  /* S-Function (slrealtimeenablelogging): '<Root>/enable_file_log' */

  /* Level2 S-Function Block: '<Root>/enable_file_log' (slrealtimeenablelogging) */
  {
    SimStruct *rts = slrt_mat_playback_M->childSfunctions[0];
    sfcnOutputs(rts,0);
  }

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++slrt_mat_playback_M->Timing.clockTick0)) {
    ++slrt_mat_playback_M->Timing.clockTickH0;
  }

  slrt_mat_playback_M->Timing.t[0] = slrt_mat_playback_M->Timing.clockTick0 *
    slrt_mat_playback_M->Timing.stepSize0 +
    slrt_mat_playback_M->Timing.clockTickH0 *
    slrt_mat_playback_M->Timing.stepSize0 * 4294967296.0;

  {
    /* Update absolute timer for sample time: [0.001s, 0.0s] */
    /* The "clockTick1" counts the number of times the code of this task has
     * been executed. The absolute time is the multiplication of "clockTick1"
     * and "Timing.stepSize1". Size of "clockTick1" ensures timer will not
     * overflow during the application lifespan selected.
     * Timer of this task consists of two 32 bit unsigned integers.
     * The two integers represent the low bits Timing.clockTick1 and the high bits
     * Timing.clockTickH1. When the low bit overflows to 0, the high bits increment.
     */
    if (!(++slrt_mat_playback_M->Timing.clockTick1)) {
      ++slrt_mat_playback_M->Timing.clockTickH1;
    }

    slrt_mat_playback_M->Timing.t[1] = slrt_mat_playback_M->Timing.clockTick1 *
      slrt_mat_playback_M->Timing.stepSize1 +
      slrt_mat_playback_M->Timing.clockTickH1 *
      slrt_mat_playback_M->Timing.stepSize1 * 4294967296.0;
  }
}

/* Model initialize function */
void slrt_mat_playback_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  {
    /* Setup solver object */
    rtsiSetSimTimeStepPtr(&slrt_mat_playback_M->solverInfo,
                          &slrt_mat_playback_M->Timing.simTimeStep);
    rtsiSetTPtr(&slrt_mat_playback_M->solverInfo, &rtmGetTPtr
                (slrt_mat_playback_M));
    rtsiSetStepSizePtr(&slrt_mat_playback_M->solverInfo,
                       &slrt_mat_playback_M->Timing.stepSize0);
    rtsiSetErrorStatusPtr(&slrt_mat_playback_M->solverInfo, (&rtmGetErrorStatus
      (slrt_mat_playback_M)));
    rtsiSetRTModelPtr(&slrt_mat_playback_M->solverInfo, slrt_mat_playback_M);
  }

  rtsiSetSimTimeStep(&slrt_mat_playback_M->solverInfo, MAJOR_TIME_STEP);
  rtsiSetIsMinorTimeStepWithModeChange(&slrt_mat_playback_M->solverInfo, false);
  rtsiSetSolverName(&slrt_mat_playback_M->solverInfo,"FixedStepDiscrete");
  slrt_mat_playback_M->solverInfoPtr = (&slrt_mat_playback_M->solverInfo);

  /* Initialize timing info */
  {
    int_T *mdlTsMap = slrt_mat_playback_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;
    mdlTsMap[1] = 1;

    /* polyspace +2 MISRA2012:D4.1 [Justified:Low] "slrt_mat_playback_M points to
       static memory which is guaranteed to be non-NULL" */
    slrt_mat_playback_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    slrt_mat_playback_M->Timing.sampleTimes =
      (&slrt_mat_playback_M->Timing.sampleTimesArray[0]);
    slrt_mat_playback_M->Timing.offsetTimes =
      (&slrt_mat_playback_M->Timing.offsetTimesArray[0]);

    /* task periods */
    slrt_mat_playback_M->Timing.sampleTimes[0] = (0.0);
    slrt_mat_playback_M->Timing.sampleTimes[1] = (0.001);

    /* task offsets */
    slrt_mat_playback_M->Timing.offsetTimes[0] = (0.0);
    slrt_mat_playback_M->Timing.offsetTimes[1] = (0.0);
  }

  rtmSetTPtr(slrt_mat_playback_M, &slrt_mat_playback_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = slrt_mat_playback_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    mdlSampleHits[1] = 1;
    slrt_mat_playback_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(slrt_mat_playback_M, -1);
  slrt_mat_playback_M->Timing.stepSize0 = 0.001;
  slrt_mat_playback_M->Timing.stepSize1 = 0.001;
  slrt_mat_playback_M->solverInfoPtr = (&slrt_mat_playback_M->solverInfo);
  slrt_mat_playback_M->Timing.stepSize = (0.001);
  rtsiSetFixedStepSize(&slrt_mat_playback_M->solverInfo, 0.001);
  rtsiSetSolverMode(&slrt_mat_playback_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* block I/O */
  (void) std::memset((static_cast<void *>(&slrt_mat_playback_B)), 0,
                     sizeof(B_slrt_mat_playback_T));

  /* states (dwork) */
  (void) std::memset(static_cast<void *>(&slrt_mat_playback_DW), 0,
                     sizeof(DW_slrt_mat_playback_T));

  /* child S-Function registration */
  {
    RTWSfcnInfo *sfcnInfo = &slrt_mat_playback_M->NonInlinedSFcns.sfcnInfo;
    slrt_mat_playback_M->sfcnInfo = (sfcnInfo);
    rtssSetErrorStatusPtr(sfcnInfo, (&rtmGetErrorStatus(slrt_mat_playback_M)));
    slrt_mat_playback_M->Sizes.numSampTimes = (2);
    rtssSetNumRootSampTimesPtr(sfcnInfo,
      &slrt_mat_playback_M->Sizes.numSampTimes);
    slrt_mat_playback_M->NonInlinedSFcns.taskTimePtrs[0] = (&rtmGetTPtr
      (slrt_mat_playback_M)[0]);
    slrt_mat_playback_M->NonInlinedSFcns.taskTimePtrs[1] = (&rtmGetTPtr
      (slrt_mat_playback_M)[1]);
    rtssSetTPtrPtr(sfcnInfo,slrt_mat_playback_M->NonInlinedSFcns.taskTimePtrs);
    rtssSetTStartPtr(sfcnInfo, &rtmGetTStart(slrt_mat_playback_M));
    rtssSetTFinalPtr(sfcnInfo, &rtmGetTFinal(slrt_mat_playback_M));
    rtssSetTimeOfLastOutputPtr(sfcnInfo, &rtmGetTimeOfLastOutput
      (slrt_mat_playback_M));
    rtssSetStepSizePtr(sfcnInfo, &slrt_mat_playback_M->Timing.stepSize);
    rtssSetStopRequestedPtr(sfcnInfo, &rtmGetStopRequested(slrt_mat_playback_M));
    rtssSetDerivCacheNeedsResetPtr(sfcnInfo,
      &slrt_mat_playback_M->derivCacheNeedsReset);
    rtssSetZCCacheNeedsResetPtr(sfcnInfo,
      &slrt_mat_playback_M->zCCacheNeedsReset);
    rtssSetContTimeOutputInconsistentWithStateAtMajorStepPtr(sfcnInfo,
      &slrt_mat_playback_M->CTOutputIncnstWithState);
    rtssSetSampleHitsPtr(sfcnInfo, &slrt_mat_playback_M->Timing.sampleHits);
    rtssSetPerTaskSampleHitsPtr(sfcnInfo,
      &slrt_mat_playback_M->Timing.perTaskSampleHits);
    rtssSetSimModePtr(sfcnInfo, &slrt_mat_playback_M->simMode);
    rtssSetSolverInfoPtr(sfcnInfo, &slrt_mat_playback_M->solverInfoPtr);
  }

  slrt_mat_playback_M->Sizes.numSFcns = (1);

  /* register each child */
  {
    (void) std::memset(static_cast<void *>
                       (&slrt_mat_playback_M->NonInlinedSFcns.childSFunctions[0]),
                       0,
                       1*sizeof(SimStruct));
    slrt_mat_playback_M->childSfunctions =
      (&slrt_mat_playback_M->NonInlinedSFcns.childSFunctionPtrs[0]);
    slrt_mat_playback_M->childSfunctions[0] =
      (&slrt_mat_playback_M->NonInlinedSFcns.childSFunctions[0]);

    /* Level2 S-Function Block: slrt_mat_playback/<Root>/enable_file_log (slrealtimeenablelogging) */
    {
      SimStruct *rts = slrt_mat_playback_M->childSfunctions[0];

      /* timing info */
      time_T *sfcnPeriod = slrt_mat_playback_M->NonInlinedSFcns.Sfcn0.sfcnPeriod;
      time_T *sfcnOffset = slrt_mat_playback_M->NonInlinedSFcns.Sfcn0.sfcnOffset;
      int_T *sfcnTsMap = slrt_mat_playback_M->NonInlinedSFcns.Sfcn0.sfcnTsMap;
      (void) std::memset(static_cast<void*>(sfcnPeriod), 0,
                         sizeof(time_T)*1);
      (void) std::memset(static_cast<void*>(sfcnOffset), 0,
                         sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      {
        ssSetBlkInfo2Ptr(rts, &slrt_mat_playback_M->NonInlinedSFcns.blkInfo2[0]);
      }

      _ssSetBlkInfo2PortInfo2Ptr(rts,
        &slrt_mat_playback_M->NonInlinedSFcns.inputOutputPortInfo2[0]);

      /* Set up the mdlInfo pointer */
      ssSetRTWSfcnInfo(rts, slrt_mat_playback_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &slrt_mat_playback_M->NonInlinedSFcns.methods2[0]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &slrt_mat_playback_M->NonInlinedSFcns.methods3[0]);
      }

      /* Allocate memory of model methods 4 */
      {
        ssSetModelMethods4(rts, &slrt_mat_playback_M->NonInlinedSFcns.methods4[0]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &slrt_mat_playback_M->NonInlinedSFcns.statesInfo2
                         [0]);
        ssSetPeriodicStatesInfo(rts,
          &slrt_mat_playback_M->NonInlinedSFcns.periodicStatesInfo[0]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &slrt_mat_playback_M->NonInlinedSFcns.Sfcn0.inputPortInfo[0]);
        ssSetPortInfoForInputs(rts,
          &slrt_mat_playback_M->NonInlinedSFcns.Sfcn0.inputPortInfo[0]);
        _ssSetPortInfo2ForInputUnits(rts,
          &slrt_mat_playback_M->NonInlinedSFcns.Sfcn0.inputPortUnits[0]);
        ssSetInputPortUnit(rts, 0, 0);
        _ssSetPortInfo2ForInputCoSimAttribute(rts,
          &slrt_mat_playback_M->NonInlinedSFcns.Sfcn0.inputPortCoSimAttribute[0]);
        ssSetInputPortIsContinuousQuantity(rts, 0, 0);

        /* port 0 */
        {
          ssSetInputPortRequiredContiguous(rts, 0, 1);
          ssSetInputPortSignal(rts, 0, &slrt_mat_playback_B.file_log_enable);
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidthAsInt(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "enable_file_log");
      ssSetPath(rts, "slrt_mat_playback/enable_file_log");
      ssSetRTModel(rts,slrt_mat_playback_M);
      ssSetParentSS(rts, (NULL));
      ssSetRootSS(rts, rts);
      ssSetVersion(rts, SIMSTRUCT_VERSION_LEVEL2);

      /* registration */
      slrealtimeenablelogging(rts);
      sfcnInitializeSizes(rts);
      sfcnInitializeSampleTimes(rts);

      /* adjust sample time */
      ssSetSampleTime(rts, 0, 0.001);
      ssSetOffsetTime(rts, 0, 0.0);
      sfcnTsMap[0] = 1;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCsAsInt(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 1);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }
  }

  /* Start for ToAsyncQueueBlock generated from: '<S1>/replay_left_torque_lookup' */
  slrt_mat_playback_DW.TAQSigLogging_InsertedFor_rep_m.SLRTSigHandles =
    slrtRegisterSignalToLoggingService(reinterpret_cast<uintptr_t>
    (&slrt_mat_playback_B.replay_left_torque_filelog));

  /* Start for ToAsyncQueueBlock generated from: '<S2>/replay_phi_lookup' */
  slrt_mat_playback_DW.TAQSigLogging_InsertedFor_rep_c.SLRTSigHandles =
    slrtRegisterSignalToLoggingService(reinterpret_cast<uintptr_t>
    (&slrt_mat_playback_B.replay_phi_filelog));

  /* Start for ToAsyncQueueBlock generated from: '<S3>/replay_right_torque_lookup' */
  slrt_mat_playback_DW.TAQSigLogging_InsertedFor_rep_k.SLRTSigHandles =
    slrtRegisterSignalToLoggingService(reinterpret_cast<uintptr_t>
    (&slrt_mat_playback_B.replay_right_torque_filelog));

  /* Start for Constant: '<Root>/file_log_enable' */
  slrt_mat_playback_B.file_log_enable =
    slrt_mat_playback_cal->file_log_enable_Value;

  /* Start for S-Function (slrealtimeenablelogging): '<Root>/enable_file_log' */
  /* Level2 S-Function Block: '<Root>/enable_file_log' (slrealtimeenablelogging) */
  {
    SimStruct *rts = slrt_mat_playback_M->childSfunctions[0];
    sfcnStart(rts);
    if (ssGetErrorStatus(rts) != (NULL))
      return;
  }
}

/* Model terminate function */
void slrt_mat_playback_terminate(void)
{
  /* Terminate for S-Function (slrealtimeenablelogging): '<Root>/enable_file_log' */
  /* Level2 S-Function Block: '<Root>/enable_file_log' (slrealtimeenablelogging) */
  {
    SimStruct *rts = slrt_mat_playback_M->childSfunctions[0];
    sfcnTerminate(rts);
  }
}
