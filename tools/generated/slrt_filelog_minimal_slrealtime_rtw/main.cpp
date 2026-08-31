/* Main generated for Simulink Real-Time model slrt_filelog_minimal */
#include <ModelInfo.hpp>
#include <utilities.hpp>
#include "rte_slrt_filelog_minimal_parameters.h"
#include "slrt_filelog_minimal.h"

/* Task wrapper function definitions */
void slrt_filelog_minimal_Task1(void)
{ 
    slrt_filelog_minimal_step();
} 
/* Task descriptors */
slrealtime::TaskInfo task_1( 0u, std::bind(slrt_filelog_minimal_Task1), slrealtime::TaskInfo::PERIODIC, 0.001, 0, 40);

/* Executable base address for XCP */
#ifdef __linux__
extern char __executable_start;
static uintptr_t const base_address = reinterpret_cast<uintptr_t>(&__executable_start);
#else
/* Set 0 as placeholder, to be parsed later from /proc filesystem */
static uintptr_t const base_address = 0;
#endif

/* Model descriptor */
slrealtime::ModelInfo slrt_filelog_minimal_Info =
{
    "slrt_filelog_minimal",
    slrt_filelog_minimal_initialize,
    slrt_filelog_minimal_terminate,
    []()->char const*& { return slrt_filelog_minimal_M->errorStatus; },
    []()->unsigned char& { return slrt_filelog_minimal_M->Timing.stopRequestedFlag; },
    { task_1 },
    slrealtime::getSegmentVector()
};

int main(int argc, char *argv[]) {
    slrealtime::BaseAddress::set(base_address);
    return slrealtime::runModel(argc, argv, slrt_filelog_minimal_Info);
}
