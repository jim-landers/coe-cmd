@echo off

SET LOCALBIN="\\depot.engr.oregonstate.edu%HOMEPATH%\.local\bin"

if not exist %LOCALBIN% (
    mkdir %LOCALBIN%
)

type NUL > %LOCALBIN%\coecmd.bat
echo @echo off >> %LOCALBIN%\coecmd.bat
echo python \\depot.engr.oregonstate.edu%HOMEPATH%\coecmd\main.py %%^* >> %LOCALBIN%\coecmd.bat

@REM /.local/bin is a directory intended for adding user scripts to the $PATH on Linux.
@REM This setx command adds it to the INDIVIDUAL USER'S %PATH%, not the whole system.
setx PATH "%%PATH%%;%LOCALBIN%"

@REM pause
