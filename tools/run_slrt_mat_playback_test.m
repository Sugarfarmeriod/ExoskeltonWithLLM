%RUN_SLRT_MAT_PLAYBACK_TEST Replay selected MAT signals on Speedgoat.
% This script builds an isolated no-hardware model that replays signals
% from data/inbox/20260610-male-2.mat through lookup tables.
% It does not load, build, deploy, or start TestStructure.slx.

disp('=== SLRT MAT Playback Capture Test ===');
fprintf('MATLAB: %s\n', version);

projectRoot = fileparts(fileparts(mfilename('fullpath')));
inputMatPath = fullfile(projectRoot, 'data', 'inbox', '20260610-male-2.mat');
generatedDir = fullfile(projectRoot, 'tools', 'generated');
if ~exist(generatedDir, 'dir')
    mkdir(generatedDir);
end

mdl = 'slrt_mat_playback';
mdlPath = fullfile(generatedDir, [mdl, '.slx']);
pollCsvPath = fullfile(generatedDir, 'slrt_mat_playback_polled_samples.csv');
fileLogDatasetPath = fullfile(generatedDir, 'slrt_mat_playback_filelog_dataset.mat');
fileLogCsvPath = fullfile(generatedDir, 'slrt_mat_playback_filelog_export.csv');
diaryPath = fullfile(generatedDir, 'slrt_mat_playback_diary.txt');

for path = string({pollCsvPath, fileLogDatasetPath, fileLogCsvPath, diaryPath})
    if exist(path, 'file')
        delete(path);
    end
end
diary(diaryPath);
cleanupDiary = onCleanup(@() diary('off'));

fprintf('Input MAT: %s\n', inputMatPath);
S = load(inputMatPath, 'data');
ds = S.data;
fprintf('Dataset elements: %d\n', ds.numElements);

selected = struct( ...
    'elementIndex', {12, 37, 38}, ...
    'varName', {'replay_phi', 'replay_left_torque', 'replay_right_torque'}, ...
    'label', {'Phi_before_correction', 'LeftHipMotorTorque', 'RightHipMotorTorque'});

startOffset = 18;
maxDuration = 12;
for k = 1:numel(selected)
    element = ds.get(selected(k).elementIndex);
    values = element.Values;
    if ~isa(values, 'timeseries')
        error('Selected element %d is not a timeseries.', selected(k).elementIndex);
    end
    time = double(values.Time(:));
    data = squeeze(double(values.Data));
    data = data(:);
    keep = time >= startOffset & time <= min(startOffset + maxDuration, time(end));
    time = time(keep);
    data = data(keep);
    time = time - time(1);
    assignin('base', [selected(k).varName, '_bp'], time);
    assignin('base', [selected(k).varName, '_data'], data);
    fprintf('%s from element %d: n=%d t=[%g,%g]\n', ...
        selected(k).varName, selected(k).elementIndex, numel(time), time(1), time(end));
end

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
    'StopTime', num2str(maxDuration), ...
    'SignalLogging', 'on', ...
    'SignalLoggingName', 'logsout', ...
    'streamoutrecorder', 'on', ...
    'SLRTFileLogMaxRuns', '5', ...
    'RTWVerbose', 'on');

add_block('simulink/Sources/Clock', [mdl, '/clock'], ...
    'Position', [70, 115, 110, 145]);
add_block('simulink/Sources/Constant', [mdl, '/file_log_enable'], ...
    'Position', [70, 30, 130, 60], ...
    'Value', 'true', ...
    'OutDataTypeStr', 'boolean');
add_block('slrealtimeloglib/Enable File Log', [mdl, '/enable_file_log'], ...
    'Position', [190, 25, 305, 65]);
add_line(mdl, 'file_log_enable/1', 'enable_file_log/1', 'autorouting', 'on');

y0 = 110;
for k = 1:numel(selected)
    name = selected(k).varName;
    lookupBlock = [mdl, '/', name, '_lookup'];
    terminatorBlock = [mdl, '/', name, '_terminator'];
    fileLogBlock = [mdl, '/', name, '_file_log'];

    add_block('simulink/Lookup Tables/1-D Lookup Table', lookupBlock, ...
        'Position', [220, y0, 360, y0 + 45], ...
        'BreakpointsForDimension1', [name, '_bp'], ...
        'Table', [name, '_data'], ...
        'ExtrapMethod', 'Clip');
    add_block('simulink/Sinks/Terminator', terminatorBlock, ...
        'Position', [540, y0 + 5, 570, y0 + 35]);
    add_block('slrealtimeloglib/File Log', fileLogBlock, ...
        'Position', [540, y0 + 50, 650, y0 + 80], ...
        'decimation', '10', ...
        'inputProcessing', 'Elements as channels (sample based)');

    add_line(mdl, 'clock/1', [name, '_lookup/1'], 'autorouting', 'on');
    outLine = add_line(mdl, [name, '_lookup/1'], [name, '_terminator/1'], 'autorouting', 'on');
    logLine = add_line(mdl, [name, '_lookup/1'], [name, '_file_log/1'], 'autorouting', 'on');
    set_param(outLine, 'Name', name);
    set_param(logLine, 'Name', [name, '_filelog']);

    ports = get_param(lookupBlock, 'PortHandles');
    set_param(ports.Outport, ...
        'TestPoint', 'on', ...
        'DataLogging', 'on', ...
        'DataLoggingNameMode', 'Custom', ...
        'DataLoggingName', name);

    y0 = y0 + 110;
end

save_system(mdl, mdlPath);
fprintf('Created MAT playback model: %s\n', mdlPath);

tg = slrealtime('TargetPC1');
connect(tg);
cleanupTarget = onCleanup(@() localStopAndDisconnect(tg));
disp(tg.TargetStatus);

disp('--- Build application ---');
slbuild(mdl);

disp('--- Load application to target ---');
load(tg, mdl);
disp(tg.ModelStatus);

disp('--- Start application ---');
start(tg, 'AutoImportFileLog', true, 'ExportToBaseWorkspace', true);

sampleCount = 20;
pollTime = zeros(sampleCount, 1);
polled = zeros(sampleCount, numel(selected));
for s = 1:sampleCount
    pause(0.25);
    pollTime(s) = s * 0.25;
    for k = 1:numel(selected)
        blockPath = [mdl, '/', selected(k).varName, '_lookup'];
        polled(s, k) = getsignal(tg, blockPath, 1);
    end
    fprintf('poll %02d t=%.2f', s, pollTime(s));
    for k = 1:numel(selected)
        fprintf(' %s=%g', selected(k).varName, polled(s, k));
    end
    fprintf('\n');
end

pollTable = array2table([pollTime, polled], ...
    'VariableNames', [{'time'}, {selected.varName}]);
writetable(pollTable, pollCsvPath);
fprintf('Saved polling CSV: %s\n', pollCsvPath);

disp('--- Stop application ---');
try
    stop(tg, 'AutoImportFileLog', true);
catch ME
    fprintf('stop note: %s\n', ME.message);
end
disp(tg.TargetStatus);
disp(tg.ModelStatus);

disp('--- File Log import/export ---');
disp(tg.FileLog);
try
    runInfo = list(tg.FileLog);
    disp(runInfo);
    if ~isempty(runInfo)
        runRows = find(runInfo.Application == string(mdl));
        if isempty(runRows)
            error('No File Log run found for %s.', mdl);
        end
        selectedRunIndex = runRows(end);
        beforeRunIds = Simulink.sdi.getAllRunIDs;
        import(tg.FileLog, selectedRunIndex);
        afterRunIds = Simulink.sdi.getAllRunIDs;
        newRunIds = setdiff(afterRunIds, beforeRunIds);
        if isempty(newRunIds) && ~isempty(afterRunIds)
            newRunIds = afterRunIds(end);
        end
        if ~isempty(newRunIds)
            fileLogRunId = newRunIds(end);
            fileLogDataset = Simulink.sdi.exportRun(fileLogRunId);
            save(fileLogDatasetPath, 'fileLogDataset', 'fileLogRunId');
            fileLogTable = localDatasetToTable(fileLogDataset);
            writetable(fileLogTable, fileLogCsvPath);
            fprintf('Saved File Log dataset: %s\n', fileLogDatasetPath);
            fprintf('Saved File Log CSV: %s\n', fileLogCsvPath);
            for idx = 1:fileLogDataset.numElements
                element = fileLogDataset.get(idx);
                fprintf('filelog %s n=%d\n', element.Name, numel(element.Values.Time));
            end
        end
    end
catch ME
    disp(getReport(ME, 'extended', 'hyperlinks', 'off'));
end

delete(cleanupTarget);
try
    disconnect(tg);
catch
end
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
