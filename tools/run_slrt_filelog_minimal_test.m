%RUN_SLRT_FILELOG_MINIMAL_TEST Minimal SLRT File Log diagnostic.
% This script builds an isolated no-hardware model and lets it stop
% naturally, then imports only the newest log for this application.
% It does not load, build, deploy, or start TestStructure.slx.

disp('=== SLRT Minimal File Log Test ===');
fprintf('MATLAB: %s\n', version);

projectRoot = fileparts(fileparts(mfilename('fullpath')));
generatedDir = fullfile(projectRoot, 'tools', 'generated');
if ~exist(generatedDir, 'dir')
    mkdir(generatedDir);
end

mdl = 'slrt_filelog_minimal';
mdlPath = fullfile(generatedDir, [mdl, '.slx']);
csvPath = fullfile(generatedDir, 'slrt_filelog_minimal_export.csv');
datasetPath = fullfile(generatedDir, 'slrt_filelog_minimal_dataset.mat');
diaryPath = fullfile(generatedDir, 'slrt_filelog_minimal_diary.txt');

for path = string({csvPath, datasetPath, diaryPath})
    if exist(path, 'file')
        delete(path);
    end
end
diary(diaryPath);
cleanupDiary = onCleanup(@() diary('off'));

if bdIsLoaded(mdl)
    close_system(mdl, 0);
end
if exist(mdlPath, 'file')
    delete(mdlPath);
end

cd(generatedDir);
new_system(mdl);
set_param(mdl, ...
    'SystemTargetFile', 'slrealtime.tlc', ...
    'SolverType', 'Fixed-step', ...
    'Solver', 'FixedStepDiscrete', ...
    'FixedStep', '0.001', ...
    'StopTime', '5', ...
    'SignalLogging', 'on', ...
    'SignalLoggingName', 'logsout', ...
    'SLRTFileLogMaxRuns', '10', ...
    'RTWVerbose', 'off');

add_block('simulink/Sources/Sine Wave', [mdl, '/sine_source'], ...
    'Position', [90, 60, 160, 90], ...
    'Amplitude', '1', ...
    'Frequency', '2*pi*1', ...
    'SampleTime', '0.001');
add_block('simulink/Sources/Clock', [mdl, '/clock_source'], ...
    'Position', [90, 155, 130, 185]);
add_block('simulink/Sources/Constant', [mdl, '/file_log_enable'], ...
    'Position', [90, 245, 150, 275], ...
    'Value', 'true', ...
    'OutDataTypeStr', 'boolean');
add_block('slrealtimeloglib/Enable File Log', [mdl, '/enable_file_log'], ...
    'Position', [230, 240, 345, 280]);
add_block('slrealtimeloglib/File Log', [mdl, '/sine_file_log'], ...
    'Position', [340, 60, 450, 90], ...
    'decimation', '1', ...
    'inputProcessing', 'Elements as channels (sample based)');
add_block('slrealtimeloglib/File Log', [mdl, '/clock_file_log'], ...
    'Position', [340, 155, 450, 185], ...
    'decimation', '1', ...
    'inputProcessing', 'Elements as channels (sample based)');
add_block('simulink/Sinks/Terminator', [mdl, '/sine_terminator'], ...
    'Position', [540, 60, 570, 90]);
add_block('simulink/Sinks/Terminator', [mdl, '/clock_terminator'], ...
    'Position', [540, 155, 570, 185]);

sineLine = add_line(mdl, 'sine_source/1', 'sine_file_log/1', 'autorouting', 'on');
clockLine = add_line(mdl, 'clock_source/1', 'clock_file_log/1', 'autorouting', 'on');
add_line(mdl, 'sine_source/1', 'sine_terminator/1', 'autorouting', 'on');
add_line(mdl, 'clock_source/1', 'clock_terminator/1', 'autorouting', 'on');
add_line(mdl, 'file_log_enable/1', 'enable_file_log/1', 'autorouting', 'on');
set_param(sineLine, 'Name', 'minimal_sine');
set_param(clockLine, 'Name', 'minimal_clock');

save_system(mdl, mdlPath);
fprintf('Created model: %s\n', mdlPath);

disp('--- Build application ---');
slbuild(mdl);
app = slrealtime.Application(fullfile(generatedDir, [mdl, '.mldatx']));
disp(getAllFileLogBlocks(app));

tg = slrealtime('TargetPC1');
connect(tg);
cleanupTarget = onCleanup(@() localStopAndDisconnect(tg));
disp(tg.TargetStatus);

disp('--- Load and run application ---');
load(tg, mdl);
start(tg, 'AutoImportFileLog', false);
while strcmp(tg.ModelStatus.State, 'RUNNING')
    pause(0.25);
end
disp(tg.TargetStatus);
disp(tg.ModelStatus);

disp('--- Import newest log for this application only ---');
runInfo = list(tg.FileLog);
disp(runInfo);
thisRunInfo = runInfo(runInfo.Application == string(mdl), :);
if isempty(thisRunInfo)
    error('No File Log run found for %s.', mdl);
end
runRows = find(runInfo.Application == string(mdl));
selectedRunIndex = runRows(end);
beforeRunIds = Simulink.sdi.getAllRunIDs;
import(tg.FileLog, selectedRunIndex);
afterRunIds = Simulink.sdi.getAllRunIDs;
newRunIds = setdiff(afterRunIds, beforeRunIds);
if isempty(newRunIds)
    error('File Log import did not create a new SDI run.');
end

runId = newRunIds(end);
fileLogDataset = Simulink.sdi.exportRun(runId);
save(datasetPath, 'fileLogDataset', 'runId');
fileLogTable = localDatasetToTable(fileLogDataset);
writetable(fileLogTable, csvPath);
fprintf('Saved dataset: %s\n', datasetPath);
fprintf('Saved CSV: %s\n', csvPath);
for idx = 1:fileLogDataset.numElements
    element = fileLogDataset.get(idx);
    fprintf('filelog %s n=%d\n', element.Name, numel(element.Values.Time));
end

delete(cleanupTarget);
disconnect(tg);
close_system(mdl, 0);
fprintf('Diary written to: %s\n', diaryPath);

function localStopAndDisconnect(tg)
try
    if strcmp(tg.ModelStatus.State, 'RUNNING')
        stop(tg, 'AutoImportFileLog', false);
    end
catch
end
try
    disconnect(tg);
catch
end
end

function outTable = localDatasetToTable(ds)
outTable = table();
for idx = 1:ds.numElements
    element = ds.get(idx);
    values = element.Values;
    if ~isa(values, 'timeseries')
        continue;
    end
    t = values.Time(:);
    y = values.Data(:);
    signalName = matlab.lang.makeValidName(element.Name);
    if isempty(outTable)
        outTable.time = t;
    end
    minLen = min(height(outTable), numel(y));
    if height(outTable) ~= numel(y)
        outTable = outTable(1:minLen, :);
        y = y(1:minLen);
    end
    outTable.(signalName) = y;
end
end
