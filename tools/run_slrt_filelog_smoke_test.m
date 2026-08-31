%RUN_SLRT_FILELOG_SMOKE_TEST Build and run a no-hardware SLRT capture test.
% This script creates an isolated test model with generated signals only.
% It does not load, build, deploy, or start TestStructure.slx.

disp('=== SLRT Generated-Signal Capture Smoke Test ===');
fprintf('MATLAB: %s\n', version);

projectRoot = fileparts(fileparts(mfilename('fullpath')));
generatedDir = fullfile(projectRoot, 'tools', 'generated');
if ~exist(generatedDir, 'dir')
    mkdir(generatedDir);
end

logPath = fullfile(generatedDir, 'slrt_filelog_smoke_diary.txt');
if exist(logPath, 'file')
    delete(logPath);
end
diary(logPath);
cleanupDiary = onCleanup(@() diary('off'));

mdl = 'slrt_filelog_smoke';
mdlPath = fullfile(generatedDir, [mdl, '.slx']);
captureMatPath = fullfile(generatedDir, 'slrt_filelog_smoke_capture.mat');
directCsvPath = fullfile(generatedDir, 'slrt_filelog_smoke_direct_samples.csv');
fileLogDatasetPath = fullfile(generatedDir, 'slrt_filelog_smoke_filelog_dataset.mat');
fileLogCsvPath = fullfile(generatedDir, 'slrt_filelog_smoke_filelog_export.csv');

fprintf('Generated folder: %s\n', generatedDir);
fprintf('Smoke model path: %s\n', mdlPath);

if bdIsLoaded(mdl)
    close_system(mdl, 0);
end

if exist(mdlPath, 'file')
    delete(mdlPath);
end
if exist(captureMatPath, 'file')
    delete(captureMatPath);
end
if exist(directCsvPath, 'file')
    delete(directCsvPath);
end
if exist(fileLogDatasetPath, 'file')
    delete(fileLogDatasetPath);
end
if exist(fileLogCsvPath, 'file')
    delete(fileLogCsvPath);
end

cd(generatedDir);
new_system(mdl);

set_param(mdl, ...
    'SystemTargetFile', 'slrealtime.tlc', ...
    'SolverType', 'Fixed-step', ...
    'Solver', 'FixedStepDiscrete', ...
    'FixedStep', '0.001', ...
    'StopTime', '30', ...
    'SignalLogging', 'on', ...
    'SignalLoggingName', 'logsout', ...
    'streamoutrecorder', 'on', ...
    'SLRTFileLogMaxRuns', '5', ...
    'RTWVerbose', 'on');

add_block('simulink/Sources/Sine Wave', [mdl, '/smoke_sine_source'], ...
    'Position', [90, 55, 160, 85], ...
    'Amplitude', '1', ...
    'Frequency', '2*pi*1', ...
    'Phase', '0', ...
    'SampleTime', '0.001');
add_block('simulink/Sources/Constant', [mdl, '/smoke_constant_source'], ...
    'Position', [90, 140, 160, 170], ...
    'Value', '42');
add_block('simulink/Sources/Constant', [mdl, '/counter_increment_source'], ...
    'Position', [90, 300, 160, 330], ...
    'Value', '1');
add_block('simulink/Sources/Constant', [mdl, '/file_log_enable'], ...
    'Position', [80, 230, 140, 260], ...
    'Value', 'true', ...
    'OutDataTypeStr', 'boolean');
add_block('simulink/Discrete/Discrete-Time Integrator', [mdl, '/smoke_counter_integrator'], ...
    'Position', [220, 290, 280, 340], ...
    'gainval', '0.001', ...
    'InitialCondition', '0', ...
    'SampleTime', '0.001');
add_block('simulink/Sinks/Terminator', [mdl, '/sine_terminator'], ...
    'Position', [330, 55, 360, 85]);
add_block('simulink/Sinks/Terminator', [mdl, '/constant_terminator'], ...
    'Position', [330, 140, 360, 170]);
add_block('simulink/Sinks/Terminator', [mdl, '/counter_terminator'], ...
    'Position', [520, 300, 550, 330]);
add_block('slrealtimeloglib/Enable File Log', [mdl, '/enable_file_log'], ...
    'Position', [210, 225, 325, 265]);
add_block('slrealtimeloglib/File Log', [mdl, '/file_log_smoke_sine'], ...
    'Position', [330, 95, 430, 125], ...
    'decimation', '10', ...
    'inputProcessing', 'Elements as channels (sample based)');
add_block('slrealtimeloglib/File Log', [mdl, '/file_log_smoke_constant'], ...
    'Position', [330, 180, 430, 210], ...
    'decimation', '10', ...
    'inputProcessing', 'Elements as channels (sample based)');
add_block('slrealtimeloglib/File Log', [mdl, '/file_log_smoke_counter'], ...
    'Position', [520, 340, 620, 370], ...
    'decimation', '10', ...
    'inputProcessing', 'Elements as channels (sample based)');

sineLine = add_line(mdl, 'smoke_sine_source/1', 'sine_terminator/1', 'autorouting', 'on');
constantLine = add_line(mdl, 'smoke_constant_source/1', 'constant_terminator/1', 'autorouting', 'on');
add_line(mdl, 'counter_increment_source/1', 'smoke_counter_integrator/1', 'autorouting', 'on');
add_line(mdl, 'file_log_enable/1', 'enable_file_log/1', 'autorouting', 'on');
counterLine = add_line(mdl, 'smoke_counter_integrator/1', 'counter_terminator/1', 'autorouting', 'on');
sineLogLine = add_line(mdl, 'smoke_sine_source/1', 'file_log_smoke_sine/1', 'autorouting', 'on');
constantLogLine = add_line(mdl, 'smoke_constant_source/1', 'file_log_smoke_constant/1', 'autorouting', 'on');
counterLogLine = add_line(mdl, 'smoke_counter_integrator/1', 'file_log_smoke_counter/1', 'autorouting', 'on');
set_param(sineLine, 'Name', 'smoke_sine');
set_param(constantLine, 'Name', 'smoke_constant');
set_param(counterLine, 'Name', 'smoke_counter');
set_param(sineLogLine, 'Name', 'smoke_sine_filelog');
set_param(constantLogLine, 'Name', 'smoke_constant_filelog');
set_param(counterLogLine, 'Name', 'smoke_counter_filelog');

sinePortHandles = get_param([mdl, '/smoke_sine_source'], 'PortHandles');
constantPortHandles = get_param([mdl, '/smoke_constant_source'], 'PortHandles');
counterPortHandles = get_param([mdl, '/smoke_counter_integrator'], 'PortHandles');
set_param(sinePortHandles.Outport, ...
    'TestPoint', 'on', ...
    'DataLogging', 'on', ...
    'DataLoggingNameMode', 'Custom', ...
    'DataLoggingName', 'smoke_sine');
set_param(constantPortHandles.Outport, ...
    'TestPoint', 'on', ...
    'DataLogging', 'on', ...
    'DataLoggingNameMode', 'Custom', ...
    'DataLoggingName', 'smoke_constant');
set_param(counterPortHandles.Outport, ...
    'TestPoint', 'on', ...
    'DataLogging', 'on', ...
    'DataLoggingNameMode', 'Custom', ...
    'DataLoggingName', 'smoke_counter');
Simulink.sdi.markSignalForStreaming(sineLine, 'on');
Simulink.sdi.markSignalForStreaming(constantLine, 'on');

mdlLoggingInfo = Simulink.SimulationData.ModelLoggingInfo(mdl);
mdlLoggingInfo.LoggingMode = 'OverrideSignals';

sineLoggingInfo = Simulink.SimulationData.SignalLoggingInfo([mdl, '/smoke_sine_source'], 1);
sineLoggingInfo.LoggingInfo.DataLogging = true;
sineLoggingInfo.LoggingInfo.NameMode = true;
sineLoggingInfo.LoggingInfo.LoggingName = 'smoke_sine';
sineLoggingInfo.LoggingInfo.DecimateData = true;
sineLoggingInfo.LoggingInfo.Decimation = 10;

constantLoggingInfo = Simulink.SimulationData.SignalLoggingInfo([mdl, '/smoke_constant_source'], 1);
constantLoggingInfo.LoggingInfo.DataLogging = true;
constantLoggingInfo.LoggingInfo.NameMode = true;
constantLoggingInfo.LoggingInfo.LoggingName = 'smoke_constant';
constantLoggingInfo.LoggingInfo.DecimateData = true;
constantLoggingInfo.LoggingInfo.Decimation = 10;

mdlLoggingInfo.Signals = [sineLoggingInfo, constantLoggingInfo];
set_param(mdl, 'DataLoggingOverride', mdlLoggingInfo);
verifySignalAndModelPaths(mdlLoggingInfo);

save_system(mdl, mdlPath);
fprintf('[%s] Created test model.\n', datestr(now, 31));

disp('--- Target connection ---');
tg = slrealtime('TargetPC1');
connect(tg);
disp(tg.TargetStatus);

disp('--- Build application ---');
slbuild(mdl);
fprintf('[%s] Build completed.\n', datestr(now, 31));

disp('--- Load application to target ---');
load(tg, mdl);
disp(tg.ModelStatus);
fprintf('[%s] Load completed.\n', datestr(now, 31));

disp('--- Configure streaming instrument ---');
try
    removeAllInstruments(tg);
catch ME
    fprintf('removeAllInstruments note: %s\n', ME.message);
end
inst = slrealtime.Instrument(mdl);
addSignal(inst, [mdl, '/smoke_sine_source'], 1, 'Decimation', 10);
addSignal(inst, [mdl, '/smoke_constant_source'], 1, 'Decimation', 10);
addSignal(inst, [mdl, '/smoke_counter_integrator'], 1, 'Decimation', 10);
addInstrument(tg, inst);
disp('Instrument configured.');

disp('--- Start application ---');
start(tg, 'AutoImportFileLog', true, 'ExportToBaseWorkspace', true);
fprintf('[%s] Start command returned.\n', datestr(now, 31));

sampleTime = zeros(12, 1);
sineSamples = nan(12, 1);
constantSamples = nan(12, 1);
for k = 1:12
    pause(0.5);
    sampleTime(k) = k * 0.5;
    try
        sineSamples(k) = getsignal(tg, [mdl, '/smoke_sine_source'], 1);
    catch ME
        fprintf('getsigal sine note at sample %d: %s\n', k, ME.message);
    end
    try
        constantSamples(k) = getsignal(tg, [mdl, '/smoke_constant_source'], 1);
    catch ME
        fprintf('getsigal constant note at sample %d: %s\n', k, ME.message);
    end
    fprintf('sample %02d: t=%.1f sine=%g constant=%g\n', ...
        k, sampleTime(k), sineSamples(k), constantSamples(k));
end

disp('--- Read buffered streaming data ---');
captureData = getBufferedData(inst);
disp(captureData);
directSamples = table(sampleTime, sineSamples, constantSamples);
writetable(directSamples, directCsvPath);
save(captureMatPath, 'captureData', 'directSamples');
fprintf('Saved capture MAT: %s\n', captureMatPath);
fprintf('Saved direct sample CSV: %s\n', directCsvPath);

disp('--- Stop application if still running ---');
try
    stop(tg, 'AutoImportFileLog', true);
catch ME
    fprintf('stop(tg) note: %s\n', ME.message);
end
disp(tg.TargetStatus);
disp(tg.ModelStatus);

disp('--- File log status snapshot ---');
disp(tg.FileLog);
try
    runInfo = list(tg.FileLog);
    disp('File log runs:');
    disp(runInfo);
    if ~isempty(runInfo)
        beforeRunIds = Simulink.sdi.getAllRunIDs;
        import(tg.FileLog, runInfo);
        disp('Imported File Log into SDI.');
        afterRunIds = Simulink.sdi.getAllRunIDs;
        newRunIds = setdiff(afterRunIds, beforeRunIds);
        if isempty(newRunIds) && ~isempty(afterRunIds)
            newRunIds = afterRunIds(end);
        end
        if ~isempty(newRunIds)
            fileLogRunId = newRunIds(end);
            fileLogDataset = Simulink.sdi.exportRun(fileLogRunId);
            save(fileLogDatasetPath, 'fileLogDataset', 'fileLogRunId');
            fprintf('Saved File Log dataset MAT: %s\n', fileLogDatasetPath);

            fileLogTable = localDatasetToTable(fileLogDataset);
            writetable(fileLogTable, fileLogCsvPath);
            fprintf('Saved File Log CSV: %s\n', fileLogCsvPath);
        else
            disp('No SDI run ID was available after File Log import.');
        end
    end
catch ME
    disp('File log list/import note:');
    disp(getReport(ME, 'extended', 'hyperlinks', 'off'));
end

try
    removeInstrument(tg, inst);
catch ME
    fprintf('removeInstrument note: %s\n', ME.message);
end
try
    disconnect(tg);
catch ME
    fprintf('disconnect(tg) note: %s\n', ME.message);
end

close_system(mdl, 0);
fprintf('[%s] Smoke test completed.\n', datestr(now, 31));
fprintf('Diary written to: %s\n', logPath);

function outTable = localDatasetToTable(ds)
outTable = table();
for idx = 1:ds.numElements
    element = ds.get(idx);
    values = element.Values;
    if isa(values, 'timeseries')
        t = values.Time(:);
        y = values.Data;
    elseif istimetable(values)
        t = seconds(values.Properties.RowTimes - values.Properties.RowTimes(1));
        y = values{:, 1};
    else
        continue;
    end
    y = y(:);
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
