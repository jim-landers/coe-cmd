$localbin = "\\depot.engr.oregonstate.edu\Users\$env:Username\.local\bin"

if (!(test-path $localbin)) {
    New-Item -Path $localbin -ItemType "directory"
}

$batchCmds = "@echo off`npython \\depot.engr.oregonstate.edu%HOMEPATH%\coecmd\main.py %*"

New-Item -Path $localbin -Name "coecmd.bat" -ItemType "File" -Force
Out-File -FilePath "$localbin\coecmd.bat" -InputObject $batchCmds -Encoding oem

# Forced to use this modified variable with escapes added in order to properly match the substring.
# Cleaner solution needs to be investigated.
$localbinSubStr = "\\depot.engr.oregonstate.edu\\Users\\$env:Username\\.local\\bin"
if (!("$env:path" -Match "$localbinSubStr")) {
    setx PATH "$env:path;$localbin"
}
