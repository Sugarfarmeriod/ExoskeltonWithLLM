/* Main generated for Simulink Real-Time model slrt_mat_playback */
#include <ModelInfo.hpp>
#include <utilities.hpp>
#include "rte_slrt_mat_playback_parameters.h"
#include "slrt_mat_playback.h"

/* Task wrapper function definitions */
void slrt_mat_playback_Task1(void)
{ 
    slrt_mat_playback_step();
} 
/* Task descriptors */
slrealtime::TaskInfo task_1( 0u, std::bind(slrt_mat_playback_Task1), slrealtime::TaskInfo::PERIODIC, 0.001, 0, 40);

/* Executable base address for XCP */
#ifdef __linux__
extern char __executable_start;
static uintptr_t const base_address = reinterpret_cast<uintptr_t>(&__executable_start);
#else
/* Set 0 as placeholder, to be parsed later from /proc filesystem */
static uintptr_t const base_address = 0;
#endif

/* Model descriptor */
slrealtime::ModelInfo slrt_mat_playback_Info =
{
    "slrt_mat_playback",
    slrt_mat_playback_initialize,
    slrt_mat_playback_terminate,
    []()->char const*& { return slrt_mat_playback_M->errorStatus; },
    []()->unsigned char& { return slrt_mat_playback_M->Timing.stopRequestedFlag; },
    { task_1 },
    slrealtime::getSegmentVector()
};

int main(int argc, char *argv[]) {
    slrealtime::BaseAddress::set(base_address);
    return slrealtime::runModel(argc, argv, slrt_mat_playback_Info);
}
