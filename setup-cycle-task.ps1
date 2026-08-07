<#
Registers (or re-registers) the Windows Scheduled Task that runs one cycle of
the Dollar Experiment every 6 hours.

    powershell -File setup-cycle-task.ps1

Deliberate choices:

- LogonType Interactive: runs only while Stan is logged on. "Run whether user is
  logged on or not" needs a stored password, which I can't enter and wouldn't
  want stored anyway.
- No WakeToRun and no StartWhenAvailable-on-battery: this should never wake the
  machine or drain it. If the PC is off at fire time, the cycle is skipped.
- StartWhenAvailable: if the PC was off at fire time, run once at the next
  opportunity rather than silently skipping until the following window.
- ExecutionTimeLimit 1 hour: a wedged cycle gets killed rather than blocking
  every later one.

Remove it with:
    Unregister-ScheduledTask -TaskName 'Dollar Experiment Cycle' -Confirm:$false
#>

$ErrorActionPreference = 'Stop'

$TaskName = 'Dollar Experiment Cycle'
$Repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$Script = Join-Path $Repo 'run-cycle.ps1'

if (-not (Test-Path $Script)) { throw "run-cycle.ps1 not found next to this script ($Script)" }

$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$Script`"" `
    -WorkingDirectory $Repo

# Every 6 hours, forever, starting 5 minutes from now.
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(5) `
    -RepetitionInterval (New-TimeSpan -Hours 6)

$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -DontStopIfGoingOnBatteries `
    -AllowStartIfOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -MultipleInstances IgnoreNew

$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Output "removed existing task"
}

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger `
    -Settings $settings -Principal $principal `
    -Description 'Runs one autonomous cycle of the Dollar Experiment (see CYCLE.md). Every 6 hours while logged on.' | Out-Null

$t = Get-ScheduledTask -TaskName $TaskName
$i = $t | Get-ScheduledTaskInfo
Write-Output "registered '$TaskName'"
Write-Output "  state:    $($t.State)"
Write-Output "  next run: $($i.NextRunTime)"
