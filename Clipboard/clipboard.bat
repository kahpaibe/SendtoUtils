@echo off
echo %*
SETLOCAL EnableDelayedExpansion
set _var=
set _nl=^&echo.
for %%i in (%*) do (
  echo %%i
  set "_var=%%~i%_nl%!_var!"
  )
echo !_var! | clip
::pause
