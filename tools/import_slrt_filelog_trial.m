function outputDir = import_slrt_filelog_trial(trialId, appName, options)
%IMPORT_SLRT_FILELOG_TRIAL Import and archive a Speedgoat File Log run.
%
% Usage from the project root:
%   addpath('tools');
%   import_slrt_filelog_trial('trial_001', 'TestStructure');
%
% This function does not build, load, start, or stop the real-time app. It
% only connects to the target, imports an existing File Log run, and writes
% Python-readable artifacts under data/raw/<trial_id>/.

arguments
    trialId (1, 1) string
    appName (1, 1) string = ""
    options.TargetName (1, 1) string = "TargetPC1"
    options.ProjectRoot (1, 1) string = string(fileparts(fileparts(mfilename('fullpath'))))
    options.RunIndex (1, 1) double = NaN
    options.SubjectId (1, 1) string = ""
    options.AffectedSide (1, 1) string = ""
    options.ParameterSnapshotPath (1, 1) string = ""
end

projectRoot = char(options.ProjectRoot);
outputDir = fullfile(projectRoot, 'data', 'raw', char(trialId));
if ~exist(outputDir, 'dir')
    mkdir(outputDir);
end

datasetPath = fullfile(outputDir, 'filelog_dataset.mat');
longCsvPath = fullfile(outputDir, 'signals_long.csv');
wideCsvPath = fullfile(outputDir, 'signals_wide_if_aligned.csv');
metadataPath = fullfile(outputDir, 'metadata.json');

tg = slrealtime(char(options.TargetName));
connect(tg);
cleanupTarget = onCleanup(@() localDisconnect(tg));

runInfo = list(tg.FileLog);
if isempty(runInfo)
    error('No File Log runs are available on target %s.', options.TargetName);
end

selectedRunIndex = options.RunIndex;
if isnan(selectedRunIndex)
    if strlength(appName) > 0
        matchingRows = find(runInfo.Application == appName);
        if isempty(matchingRows)
            error('No File Log run found for application %s.', appName);
        end
        selectedRunIndex = matchingRows(end);
    else
        selectedRunIndex = height(runInfo);
    end
end

if selectedRunIndex < 1 || selectedRunIndex > height(runInfo)
    error('RunIndex %d is outside available File Log rows 1..%d.', ...
        selectedRunIndex, height(runInfo));
end

selectedRunInfo = runInfo(selectedRunIndex, :);
beforeRunIds = Simulink.sdi.getAllRunIDs;
import(tg.FileLog, selectedRunIndex);
afterRunIds = Simulink.sdi.getAllRunIDs;
newRunIds = setdiff(afterRunIds, beforeRunIds);
if isempty(newRunIds)
    error('File Log import did not create a new SDI run.');
end

fileLogRunId = newRunIds(end);
fileLogDataset = Simulink.sdi.exportRun(fileLogRunId);
save(datasetPath, 'fileLogDataset', 'fileLogRunId', 'selectedRunInfo');

[longTable, signalSummary] = localDatasetToLongTable(fileLogDataset);
if isempty(signalSummary)
    error(['File Log import contained no supported time-series leaves. ' ...
        'Bus-valued signals must be expanded before CSV export.']);
end
writetable(longTable, longCsvPath);

[wideTable, aligned] = localDatasetToWideTable(fileLogDataset);
if aligned
    writetable(wideTable, wideCsvPath);
else
    wideCsvPath = "";
end

metadata = struct();
metadata.trial_id = char(trialId);
metadata.application = char(selectedRunInfo.Application);
metadata.target_name = char(options.TargetName);
metadata.import_time = char(datetime('now', 'TimeZone', 'local', 'Format', 'yyyy-MM-dd HH:mm:ss Z'));
metadata.source_start_date = char(selectedRunInfo.StartDate);
metadata.source_size_mb = selectedRunInfo.("Size (in MB)");
metadata.subject_id = char(options.SubjectId);
metadata.affected_side = char(options.AffectedSide);
metadata.parameter_snapshot_path = char(options.ParameterSnapshotPath);
metadata.filelog_run_id = fileLogRunId;
metadata.dataset_mat = datasetPath;
metadata.signals_long_csv = longCsvPath;
metadata.signals_wide_csv = char(wideCsvPath);
metadata.signals_are_time_aligned = aligned;
metadata.signal_count = numel(signalSummary);
metadata.signals = signalSummary;

fid = fopen(metadataPath, 'w');
if fid < 0
    error('Could not open metadata file for writing: %s', metadataPath);
end
cleanupFile = onCleanup(@() fclose(fid));
fprintf(fid, '%s', jsonencode(metadata, PrettyPrint=true));
delete(cleanupFile);

delete(cleanupTarget);
disconnect(tg);

fprintf('Archived File Log trial to: %s\n', outputDir);
fprintf('  MAT:  %s\n', datasetPath);
fprintf('  CSV:  %s\n', longCsvPath);
if aligned
    fprintf('  Wide: %s\n', wideCsvPath);
end
fprintf('  JSON: %s\n', metadataPath);
end

function localDisconnect(tg)
try
    disconnect(tg);
catch
end
end

function [outTable, signalSummary] = localDatasetToLongTable(ds)
signalCol = strings(0, 1);
timeCol = zeros(0, 1);
valueCol = zeros(0, 1);
elementCol = zeros(0, 1);
signalSummary = struct('name', {}, 'sample_count', {}, 'start_time', {}, 'end_time', {});

for idx = 1:ds.numElements
    element = ds.get(idx);
    leaves = localFlattenTimeseries(element.Values, string(element.Name));

    for leafIdx = 1:numel(leaves)
        values = leaves(leafIdx).values;
        t = double(values.Time(:));
        y = squeeze(double(values.Data));
        y = y(:);
        n = min(numel(t), numel(y));
        t = t(1:n);
        y = y(1:n);
        name = string(leaves(leafIdx).name);

        signalCol = [signalCol; repmat(name, n, 1)]; %#ok<AGROW>
        timeCol = [timeCol; t]; %#ok<AGROW>
        valueCol = [valueCol; y]; %#ok<AGROW>
        elementCol = [elementCol; repmat(idx, n, 1)]; %#ok<AGROW>

        summary = struct();
        summary.name = char(name);
        summary.sample_count = n;
        if n > 0
            summary.start_time = t(1);
            summary.end_time = t(end);
        else
            summary.start_time = NaN;
            summary.end_time = NaN;
        end
        signalSummary(end + 1) = summary; %#ok<AGROW>
    end
end

outTable = table(signalCol, timeCol, valueCol, elementCol, ...
    'VariableNames', {'signal', 'time', 'value', 'element_index'});
end

function [outTable, aligned] = localDatasetToWideTable(ds)
outTable = table();
referenceTime = [];
aligned = true;

for idx = 1:ds.numElements
    element = ds.get(idx);
    leaves = localFlattenTimeseries(element.Values, string(element.Name));

    for leafIdx = 1:numel(leaves)
        values = leaves(leafIdx).values;
        t = double(values.Time(:));
        y = squeeze(double(values.Data));
        y = y(:);
        n = min(numel(t), numel(y));
        t = t(1:n);
        y = y(1:n);

        if isempty(referenceTime)
            referenceTime = t;
            outTable.time = t;
        elseif numel(t) ~= numel(referenceTime) || any(abs(t - referenceTime) > 1e-12)
            aligned = false;
            outTable = table();
            return;
        end

        signalName = matlab.lang.makeValidName(leaves(leafIdx).name);
        signalName = matlab.lang.makeUniqueStrings(signalName, ...
            outTable.Properties.VariableNames);
        outTable.(signalName) = y;
    end
end
end

function leaves = localFlattenTimeseries(value, prefix)
leaves = struct('name', {}, 'values', {});

if isa(value, 'timeseries')
    leaf = struct();
    leaf.name = char(prefix);
    leaf.values = value;
    leaves = leaf;
    return;
end

if ~isstruct(value) || ~isscalar(value)
    return;
end

fields = fieldnames(value);
for idx = 1:numel(fields)
    fieldName = fields{idx};
    if strlength(prefix) > 0
        childPrefix = prefix + "." + string(fieldName);
    else
        childPrefix = string(fieldName);
    end
    childLeaves = localFlattenTimeseries(value.(fieldName), childPrefix);
    leaves = [leaves childLeaves]; %#ok<AGROW>
end
end
