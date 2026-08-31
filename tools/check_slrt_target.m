%CHECK_SLRT_TARGET Read-only Simulink Real-Time target diagnostics.
% Run from MATLAB after connecting the Speedgoat Ethernet link.
% This script does not update, install, load, start, or stop the target.

disp('=== Simulink Real-Time Target Diagnostics ===');
fprintf('MATLAB: %s\n', version);
fprintf('Working folder: %s\n', pwd);

try
    tg = slrealtime;
catch ME
    fprintf('Failed to create slrealtime target object:\n%s\n', getReport(ME, 'basic'));
    return;
end

disp('--- Target settings ---');
disp(tg.TargetSettings);

targetAddress = string(tg.TargetSettings.address);
if strlength(targetAddress) > 0
    fprintf('Pinging target address %s...\n', targetAddress);
    [status, output] = system("ping -n 2 " + targetAddress);
    fprintf('%s\n', output);
    if status ~= 0
        fprintf('Ping failed for %s.\n', targetAddress);
    end
else
    fprintf('Target address is empty.\n');
end

disp('--- Connection attempt ---');
try
    connect(tg);
    disp('connect(tg) succeeded.');
catch ME
    fprintf('connect(tg) failed:\n%s\n', getReport(ME, 'extended', 'hyperlinks', 'off'));
end

disp('--- Target status snapshot ---');
try
    disp(tg.TargetStatus);
catch ME
    fprintf('Unable to read TargetStatus: %s\n', ME.message);
end

try
    disp(tg.ModelStatus);
catch ME
    fprintf('Unable to read ModelStatus: %s\n', ME.message);
end

try
    disp(tg.FileLog);
catch ME
    fprintf('Unable to read FileLog: %s\n', ME.message);
end
