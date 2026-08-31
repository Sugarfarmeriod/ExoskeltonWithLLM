/*
 * slrt_filelog_smoke.cpp
 *
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * Code generation for model "slrt_filelog_smoke".
 *
 * Model version              : 1.1
 * Simulink Coder version : 23.2 (R2023b) 01-Aug-2023
 * C++ source code generated on : Mon Jun 29 17:51:55 2026
 *
 * Target selection: slrealtime.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: Intel->x86-64 (Linux 64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "slrt_filelog_smoke.h"
#include "rtwtypes.h"
#include "slrt_filelog_smoke_cal.h"
#include <cmath>
#include "slrt_filelog_smoke_private.h"
#include <cstring>

extern "C"
{

#include "rt_nonfinite.h"

}

const boolean_T slrt_filelog_smoke_BGND = false;/* boolean_T ground */

/* Block signals (default storage) */
B_slrt_filelog_smoke_T slrt_filelog_smoke_B;

/* Block states (default storage) */
DW_slrt_filelog_smoke_T slrt_filelog_smoke_DW;

/* Real-time model */
RT_MODEL_slrt_filelog_smoke_T slrt_filelog_smoke_M_ =
  RT_MODEL_slrt_filelog_smoke_T();
RT_MODEL_slrt_filelog_smoke_T *const slrt_filelog_smoke_M =
  &slrt_filelog_smoke_M_;

/* Model step function */
void slrt_filelog_smoke_step(void)
{
  real_T HoldCosine;
  real_T lastSin_tmp;

  /* Constant: '<Root>/smoke_constant_source' */
  slrt_filelog_smoke_B.smoke_constant_filelog =
    slrt_filelog_smoke_cal->smoke_constant_source_Value;

  /* ToAsyncQueueBlock generated from: '<S1>/smoke_constant_source' */
  slrtLogSignal
    (slrt_filelog_smoke_DW.TAQSigLogging_InsertedFor_smo_c.SLRTSigHandles,
     slrt_filelog_smoke_M->Timing.t[0]);

  /* DiscreteIntegrator: '<Root>/smoke_counter_integrator' */
  slrt_filelog_smoke_B.smoke_counter_filelog =
    slrt_filelog_smoke_DW.smoke_counter_integrator_DSTATE;

  /* ToAsyncQueueBlock generated from: '<S2>/smoke_counter_integrator' */
  slrtLogSignal
    (slrt_filelog_smoke_DW.TAQSigLogging_InsertedFor_smo_f.SLRTSigHandles,
     slrt_filelog_smoke_M->Timing.t[0]);

  /* Sin: '<Root>/smoke_sine_source' */
  if (slrt_filelog_smoke_DW.systemEnable != 0) {
    lastSin_tmp = slrt_filelog_smoke_cal->smoke_sine_source_Freq *
      slrt_filelog_smoke_M->Timing.t[0];
    slrt_filelog_smoke_DW.lastSin = std::sin(lastSin_tmp);
    slrt_filelog_smoke_DW.lastCos = std::cos(lastSin_tmp);
    slrt_filelog_smoke_DW.systemEnable = 0;
  }

  /* Sin: '<Root>/smoke_sine_source' */
  slrt_filelog_smoke_B.smoke_sine_filelog = ((slrt_filelog_smoke_DW.lastSin *
    slrt_filelog_smoke_cal->smoke_sine_source_PCos +
    slrt_filelog_smoke_DW.lastCos *
    slrt_filelog_smoke_cal->smoke_sine_source_PSin) *
    slrt_filelog_smoke_cal->smoke_sine_source_HCos +
    (slrt_filelog_smoke_DW.lastCos *
     slrt_filelog_smoke_cal->smoke_sine_source_PCos -
     slrt_filelog_smoke_DW.lastSin *
     slrt_filelog_smoke_cal->smoke_sine_source_PSin) *
    slrt_filelog_smoke_cal->smoke_sine_source_Hsin) *
    slrt_filelog_smoke_cal->smoke_sine_source_Amp +
    slrt_filelog_smoke_cal->smoke_sine_source_Bias;

  /* ToAsyncQueueBlock generated from: '<S3>/smoke_sine_source' */
  slrtLogSignal
    (slrt_filelog_smoke_DW.TAQSigLogging_InsertedFor_sm_f1.SLRTSigHandles,
     slrt_filelog_smoke_M->Timing.t[0]);

  /* S-Function (slrealtimeenablelogging): '<Root>/enable_file_log' */

  /* Level2 S-Function Block: '<Root>/enable_file_log' (slrealtimeenablelogging) */
  {
    SimStruct *rts = slrt_filelog_smoke_M->childSfunctions[0];
    sfcnOutputs(rts,0);
  }

  /* Update for DiscreteIntegrator: '<Root>/smoke_counter_integrator' incorporates:
   *  Constant: '<Root>/counter_increment_source'
   */
  slrt_filelog_smoke_DW.smoke_counter_integrator_DSTATE +=
    slrt_filelog_smoke_cal->smoke_counter_integrator_gainva *
    slrt_filelog_smoke_cal->counter_increment_source_Value;

  /* Update for Sin: '<Root>/smoke_sine_source' */
  lastSin_tmp = slrt_filelog_smoke_DW.lastSin;
  HoldCosine = slrt_filelog_smoke_DW.lastCos;
  slrt_filelog_smoke_DW.lastSin = lastSin_tmp *
    slrt_filelog_smoke_cal->smoke_sine_source_HCos + HoldCosine *
    slrt_filelog_smoke_cal->smoke_sine_source_Hsin;
  slrt_filelog_smoke_DW.lastCos = HoldCosine *
    slrt_filelog_smoke_cal->smoke_sine_source_HCos - lastSin_tmp *
    slrt_filelog_smoke_cal->smoke_sine_source_Hsin;

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++slrt_filelog_smoke_M->Timing.clockTick0)) {
    ++slrt_filelog_smoke_M->Timing.clockTickH0;
  }

  slrt_filelog_smoke_M->Timing.t[0] = slrt_filelog_smoke_M->Timing.clockTick0 *
    slrt_filelog_smoke_M->Timing.stepSize0 +
    slrt_filelog_smoke_M->Timing.clockTickH0 *
    slrt_filelog_smoke_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void slrt_filelog_smoke_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));
  rtsiSetSolverName(&slrt_filelog_smoke_M->solverInfo,"FixedStepDiscrete");
  slrt_filelog_smoke_M->solverInfoPtr = (&slrt_filelog_smoke_M->solverInfo);

  /* Initialize timing info */
  {
    int_T *mdlTsMap = slrt_filelog_smoke_M->Timing.sampleTimeTaskIDArray;
    mdlTsMap[0] = 0;

    /* polyspace +2 MISRA2012:D4.1 [Justified:Low] "slrt_filelog_smoke_M points to
       static memory which is guaranteed to be non-NULL" */
    slrt_filelog_smoke_M->Timing.sampleTimeTaskIDPtr = (&mdlTsMap[0]);
    slrt_filelog_smoke_M->Timing.sampleTimes =
      (&slrt_filelog_smoke_M->Timing.sampleTimesArray[0]);
    slrt_filelog_smoke_M->Timing.offsetTimes =
      (&slrt_filelog_smoke_M->Timing.offsetTimesArray[0]);

    /* task periods */
    slrt_filelog_smoke_M->Timing.sampleTimes[0] = (0.001);

    /* task offsets */
    slrt_filelog_smoke_M->Timing.offsetTimes[0] = (0.0);
  }

  rtmSetTPtr(slrt_filelog_smoke_M, &slrt_filelog_smoke_M->Timing.tArray[0]);

  {
    int_T *mdlSampleHits = slrt_filelog_smoke_M->Timing.sampleHitArray;
    mdlSampleHits[0] = 1;
    slrt_filelog_smoke_M->Timing.sampleHits = (&mdlSampleHits[0]);
  }

  rtmSetTFinal(slrt_filelog_smoke_M, -1);
  slrt_filelog_smoke_M->Timing.stepSize0 = 0.001;
  slrt_filelog_smoke_M->solverInfoPtr = (&slrt_filelog_smoke_M->solverInfo);
  slrt_filelog_smoke_M->Timing.stepSize = (0.001);
  rtsiSetFixedStepSize(&slrt_filelog_smoke_M->solverInfo, 0.001);
  rtsiSetSolverMode(&slrt_filelog_smoke_M->solverInfo, SOLVER_MODE_SINGLETASKING);

  /* block I/O */
  (void) std::memset((static_cast<void *>(&slrt_filelog_smoke_B)), 0,
                     sizeof(B_slrt_filelog_smoke_T));

  /* states (dwork) */
  (void) std::memset(static_cast<void *>(&slrt_filelog_smoke_DW), 0,
                     sizeof(DW_slrt_filelog_smoke_T));

  /* child S-Function registration */
  {
    RTWSfcnInfo *sfcnInfo = &slrt_filelog_smoke_M->NonInlinedSFcns.sfcnInfo;
    slrt_filelog_smoke_M->sfcnInfo = (sfcnInfo);
    rtssSetErrorStatusPtr(sfcnInfo, (&rtmGetErrorStatus(slrt_filelog_smoke_M)));
    slrt_filelog_smoke_M->Sizes.numSampTimes = (1);
    rtssSetNumRootSampTimesPtr(sfcnInfo,
      &slrt_filelog_smoke_M->Sizes.numSampTimes);
    slrt_filelog_smoke_M->NonInlinedSFcns.taskTimePtrs[0] = (&rtmGetTPtr
      (slrt_filelog_smoke_M)[0]);
    rtssSetTPtrPtr(sfcnInfo,slrt_filelog_smoke_M->NonInlinedSFcns.taskTimePtrs);
    rtssSetTStartPtr(sfcnInfo, &rtmGetTStart(slrt_filelog_smoke_M));
    rtssSetTFinalPtr(sfcnInfo, &rtmGetTFinal(slrt_filelog_smoke_M));
    rtssSetTimeOfLastOutputPtr(sfcnInfo, &rtmGetTimeOfLastOutput
      (slrt_filelog_smoke_M));
    rtssSetStepSizePtr(sfcnInfo, &slrt_filelog_smoke_M->Timing.stepSize);
    rtssSetStopRequestedPtr(sfcnInfo, &rtmGetStopRequested(slrt_filelog_smoke_M));
    rtssSetDerivCacheNeedsResetPtr(sfcnInfo,
      &slrt_filelog_smoke_M->derivCacheNeedsReset);
    rtssSetZCCacheNeedsResetPtr(sfcnInfo,
      &slrt_filelog_smoke_M->zCCacheNeedsReset);
    rtssSetContTimeOutputInconsistentWithStateAtMajorStepPtr(sfcnInfo,
      &slrt_filelog_smoke_M->CTOutputIncnstWithState);
    rtssSetSampleHitsPtr(sfcnInfo, &slrt_filelog_smoke_M->Timing.sampleHits);
    rtssSetPerTaskSampleHitsPtr(sfcnInfo,
      &slrt_filelog_smoke_M->Timing.perTaskSampleHits);
    rtssSetSimModePtr(sfcnInfo, &slrt_filelog_smoke_M->simMode);
    rtssSetSolverInfoPtr(sfcnInfo, &slrt_filelog_smoke_M->solverInfoPtr);
  }

  slrt_filelog_smoke_M->Sizes.numSFcns = (1);

  /* register each child */
  {
    (void) std::memset(static_cast<void *>
                       (&slrt_filelog_smoke_M->NonInlinedSFcns.childSFunctions[0]),
                       0,
                       1*sizeof(SimStruct));
    slrt_filelog_smoke_M->childSfunctions =
      (&slrt_filelog_smoke_M->NonInlinedSFcns.childSFunctionPtrs[0]);
    slrt_filelog_smoke_M->childSfunctions[0] =
      (&slrt_filelog_smoke_M->NonInlinedSFcns.childSFunctions[0]);

    /* Level2 S-Function Block: slrt_filelog_smoke/<Root>/enable_file_log (slrealtimeenablelogging) */
    {
      SimStruct *rts = slrt_filelog_smoke_M->childSfunctions[0];

      /* timing info */
      time_T *sfcnPeriod =
        slrt_filelog_smoke_M->NonInlinedSFcns.Sfcn0.sfcnPeriod;
      time_T *sfcnOffset =
        slrt_filelog_smoke_M->NonInlinedSFcns.Sfcn0.sfcnOffset;
      int_T *sfcnTsMap = slrt_filelog_smoke_M->NonInlinedSFcns.Sfcn0.sfcnTsMap;
      (void) std::memset(static_cast<void*>(sfcnPeriod), 0,
                         sizeof(time_T)*1);
      (void) std::memset(static_cast<void*>(sfcnOffset), 0,
                         sizeof(time_T)*1);
      ssSetSampleTimePtr(rts, &sfcnPeriod[0]);
      ssSetOffsetTimePtr(rts, &sfcnOffset[0]);
      ssSetSampleTimeTaskIDPtr(rts, sfcnTsMap);

      {
        ssSetBlkInfo2Ptr(rts, &slrt_filelog_smoke_M->NonInlinedSFcns.blkInfo2[0]);
      }

      _ssSetBlkInfo2PortInfo2Ptr(rts,
        &slrt_filelog_smoke_M->NonInlinedSFcns.inputOutputPortInfo2[0]);

      /* Set up the mdlInfo pointer */
      ssSetRTWSfcnInfo(rts, slrt_filelog_smoke_M->sfcnInfo);

      /* Allocate memory of model methods 2 */
      {
        ssSetModelMethods2(rts, &slrt_filelog_smoke_M->NonInlinedSFcns.methods2
                           [0]);
      }

      /* Allocate memory of model methods 3 */
      {
        ssSetModelMethods3(rts, &slrt_filelog_smoke_M->NonInlinedSFcns.methods3
                           [0]);
      }

      /* Allocate memory of model methods 4 */
      {
        ssSetModelMethods4(rts, &slrt_filelog_smoke_M->NonInlinedSFcns.methods4
                           [0]);
      }

      /* Allocate memory for states auxilliary information */
      {
        ssSetStatesInfo2(rts, &slrt_filelog_smoke_M->
                         NonInlinedSFcns.statesInfo2[0]);
        ssSetPeriodicStatesInfo(rts,
          &slrt_filelog_smoke_M->NonInlinedSFcns.periodicStatesInfo[0]);
      }

      /* inputs */
      {
        _ssSetNumInputPorts(rts, 1);
        ssSetPortInfoForInputs(rts,
          &slrt_filelog_smoke_M->NonInlinedSFcns.Sfcn0.inputPortInfo[0]);
        ssSetPortInfoForInputs(rts,
          &slrt_filelog_smoke_M->NonInlinedSFcns.Sfcn0.inputPortInfo[0]);
        _ssSetPortInfo2ForInputUnits(rts,
          &slrt_filelog_smoke_M->NonInlinedSFcns.Sfcn0.inputPortUnits[0]);
        ssSetInputPortUnit(rts, 0, 0);
        _ssSetPortInfo2ForInputCoSimAttribute(rts,
          &slrt_filelog_smoke_M->NonInlinedSFcns.Sfcn0.inputPortCoSimAttribute[0]);
        ssSetInputPortIsContinuousQuantity(rts, 0, 0);

        /* port 0 */
        {
          ssSetInputPortRequiredContiguous(rts, 0, 1);
          ssSetInputPortSignal(rts, 0, (const_cast<boolean_T*>
            (&slrt_filelog_smoke_BGND)));
          _ssSetInputPortNumDimensions(rts, 0, 1);
          ssSetInputPortWidthAsInt(rts, 0, 1);
        }
      }

      /* path info */
      ssSetModelName(rts, "enable_file_log");
      ssSetPath(rts, "slrt_filelog_smoke/enable_file_log");
      ssSetRTModel(rts,slrt_filelog_smoke_M);
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
      sfcnTsMap[0] = 0;

      /* set compiled values of dynamic vector attributes */
      ssSetNumNonsampledZCsAsInt(rts, 0);

      /* Update connectivity flags for each port */
      _ssSetInputPortConnected(rts, 0, 0);

      /* Update the BufferDstPort flags for each input port */
      ssSetInputPortBufferDstPort(rts, 0, -1);
    }
  }

  /* Start for ToAsyncQueueBlock generated from: '<S1>/smoke_constant_source' */
  slrt_filelog_smoke_DW.TAQSigLogging_InsertedFor_smo_c.SLRTSigHandles =
    slrtRegisterSignalToLoggingService(reinterpret_cast<uintptr_t>
    (&slrt_filelog_smoke_B.smoke_constant_filelog));

  /* Start for ToAsyncQueueBlock generated from: '<S2>/smoke_counter_integrator' */
  slrt_filelog_smoke_DW.TAQSigLogging_InsertedFor_smo_f.SLRTSigHandles =
    slrtRegisterSignalToLoggingService(reinterpret_cast<uintptr_t>
    (&slrt_filelog_smoke_B.smoke_counter_filelog));

  /* Start for ToAsyncQueueBlock generated from: '<S3>/smoke_sine_source' */
  slrt_filelog_smoke_DW.TAQSigLogging_InsertedFor_sm_f1.SLRTSigHandles =
    slrtRegisterSignalToLoggingService(reinterpret_cast<uintptr_t>
    (&slrt_filelog_smoke_B.smoke_sine_filelog));

  /* Start for S-Function (slrealtimeenablelogging): '<Root>/enable_file_log' */
  /* Level2 S-Function Block: '<Root>/enable_file_log' (slrealtimeenablelogging) */
  {
    SimStruct *rts = slrt_filelog_smoke_M->childSfunctions[0];
    sfcnStart(rts);
    if (ssGetErrorStatus(rts) != (NULL))
      return;
  }

  /* InitializeConditions for DiscreteIntegrator: '<Root>/smoke_counter_integrator' */
  slrt_filelog_smoke_DW.smoke_counter_integrator_DSTATE =
    slrt_filelog_smoke_cal->smoke_counter_integrator_IC;

  /* Enable for Sin: '<Root>/smoke_sine_source' */
  slrt_filelog_smoke_DW.systemEnable = 1;
}

/* Model terminate function */
void slrt_filelog_smoke_terminate(void)
{
  /* Terminate for S-Function (slrealtimeenablelogging): '<Root>/enable_file_log' */
  /* Level2 S-Function Block: '<Root>/enable_file_log' (slrealtimeenablelogging) */
  {
    SimStruct *rts = slrt_filelog_smoke_M->childSfunctions[0];
    sfcnTerminate(rts);
  }
}
