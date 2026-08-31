bdclose('all');
scriptDir = fileparts(mfilename('fullpath'));
projectDir = fileparts(scriptDir);
cd(projectDir);
load_system(fullfile(projectDir, 'TestStructure.slx'));

sub = 'TestStructure/InterForceControlTask';
outDir = fullfile(projectDir, 'analysis_outputs');
if ~exist(outDir, 'dir')
    mkdir(outDir);
end

moBlocks = find_system(sub, ...
    'LookUnderMasks', 'all', ...
    'FollowLinks', 'on', ...
    'MatchFilter', @Simulink.match.allVariants, ...
    'RegExp', 'on', ...
    'Name', '^MO_.*');

moRows = {};
for i = 1:numel(moBlocks)
    b = moBlocks{i};
    bt = gp(b, 'BlockType');
    key = blockKeyParam(b, bt);
    [srcs, dsts] = blockNeighbors(b);
    moRows(end+1,:) = {gp(b, 'Name'), bt, gp(b, 'Parent'), key, srcs, dsts, b}; %#ok<SAGROW>
end
moTable = cell2table(moRows, 'VariableNames', ...
    {'Name','BlockType','Parent','Parameter','Sources','Destinations','Path'});
writetable(moTable, fullfile(outDir, 'interforce_mo_blocks.csv'));

lines = find_system(sub, ...
    'LookUnderMasks', 'all', ...
    'FollowLinks', 'on', ...
    'MatchFilter', @Simulink.match.allVariants, ...
    'FindAll', 'on', ...
    'Type', 'line');

lineRows = {};
for k = 1:numel(lines)
    nm = gp(lines(k), 'Name');
    if contains(nm, 'MO_')
        src = get_param(lines(k), 'SrcBlockHandle');
        srcn = '';
        if ~isempty(src) && src ~= -1 && ishandle(src)
            srcn = oneLine(getfullname(src));
        end
        dst = get_param(lines(k), 'DstBlockHandle');
        dstn = {};
        for j = 1:numel(dst)
            if dst(j) ~= -1 && ishandle(dst(j))
                dstn{end+1} = oneLine(getfullname(dst(j))); %#ok<SAGROW>
            end
        end
        lineRows(end+1,:) = {nm, srcn, strjoin(dstn, '; ')}; %#ok<SAGROW>
    end
end
if isempty(lineRows)
    lineTable = cell2table(cell(0,3), 'VariableNames', {'Name','Source','Destinations'});
else
    lineTable = cell2table(lineRows, 'VariableNames', {'Name','Source','Destinations'});
end
writetable(lineTable, fullfile(outDir, 'interforce_mo_lines.csv'));

blocks = find_system(sub, ...
    'LookUnderMasks', 'all', ...
    'FollowLinks', 'on', ...
    'MatchFilter', @Simulink.match.allVariants, ...
    'Type', 'block');

interesting = {'Constant','Gain','Saturate','Switch','ManualSwitch','UnitDelay','Memory', ...
    'DiscreteFilter','DiscreteTransferFcn','TransferFcn','Integrator','DiscreteIntegrator', ...
    'Relay','DeadZone','Lookup_n-D','PreLookup','Interpolation_n-D','RateLimiter'};
candidateRows = {};
for i = 1:numel(blocks)
    b = blocks{i};
    name = gp(b, 'Name');
    if startsWith(name, 'MO_')
        continue;
    end
    bt = gp(b, 'BlockType');
    if ~any(strcmp(bt, interesting))
        continue;
    end
    key = blockKeyParam(b, bt);
    [srcs, dsts] = blockNeighbors(b);
    candidateRows(end+1,:) = {name, bt, gp(b, 'Parent'), key, srcs, dsts, b}; %#ok<SAGROW>
end
candidateTable = cell2table(candidateRows, 'VariableNames', ...
    {'Name','BlockType','Parent','Parameter','Sources','Destinations','Path'});
writetable(candidateTable, fullfile(outDir, 'interforce_non_mo_candidates.csv'));

subsystems = find_system(sub, ...
    'LookUnderMasks', 'all', ...
    'FollowLinks', 'on', ...
    'MatchFilter', @Simulink.match.allVariants, ...
    'BlockType', 'SubSystem');
summaryRows = {};
for i = 1:numel(subsystems)
    ss = subsystems{i};
    direct = find_system(ss, 'SearchDepth', 1, 'Type', 'block');
    summaryRows(end+1,:) = {ss, numel(direct)-1}; %#ok<SAGROW>
end
summaryTable = cell2table(summaryRows, 'VariableNames', {'Subsystem','DirectChildBlocks'});
writetable(summaryTable, fullfile(outDir, 'interforce_subsystems.csv'));

disp("Wrote analysis CSV files to:");
disp(outDir);
disp(moTable);

function s = gp(obj, p)
try
    s = oneLine(get_param(obj, p));
catch
    s = '';
end
end

function s = oneLine(x)
if isnumeric(x)
    x = mat2str(x);
end
if isstring(x)
    x = char(x);
end
if iscell(x)
    x = strjoin(cellfun(@char, x, 'UniformOutput', false), ',');
end
s = char(x);
s = strrep(s, newline, ' ');
s = strtrim(s);
end

function key = blockKeyParam(b, bt)
switch bt
    case 'Constant'
        key = "Value=" + gp(b, 'Value');
    case 'Gain'
        key = "Gain=" + gp(b, 'Gain');
    case 'Saturate'
        key = "Upper=" + gp(b, 'UpperLimit') + ", Lower=" + gp(b, 'LowerLimit');
    case 'Switch'
        key = "Criteria=" + gp(b, 'Criteria') + ", Threshold=" + gp(b, 'Threshold');
    case 'ManualSwitch'
        key = "sw=" + gp(b, 'sw');
    case {'UnitDelay','Memory'}
        key = "InitialCondition=" + gp(b, 'InitialCondition');
    case 'DiscreteFilter'
        key = "Numerator=" + gp(b, 'Numerator') + ", Denominator=" + gp(b, 'Denominator');
    case 'DiscreteTransferFcn'
        key = "Numerator=" + gp(b, 'Numerator') + ", Denominator=" + gp(b, 'Denominator');
    otherwise
        key = "";
end
key = char(key);
end

function [srcs, dsts] = blockNeighbors(b)
pc = get_param(b, 'PortConnectivity');
srcList = {};
dstList = {};
for p = 1:numel(pc)
    sh = pc(p).SrcBlock;
    if ~isempty(sh) && sh ~= -1
        srcList{end+1} = oneLine(getfullname(sh)); %#ok<AGROW>
    end
    dh = pc(p).DstBlock;
    for d = 1:numel(dh)
        if dh(d) ~= -1
            dstList{end+1} = oneLine(getfullname(dh(d))); %#ok<AGROW>
        end
    end
end
srcs = strjoin(unique(srcList), '; ');
dsts = strjoin(unique(dstList), '; ');
end
