@echo off

:: Reset variables
set "plugin_id="
set "plugin_name="

:: Get variables from user input
set /p plugin_id=Enter plugin ID (default to plugin_id): 
set /p plugin_name=Enter plugin name (default to plugin_name): 

if "%plugin_id%" == "" set plugin_id=plugin_id
if "%plugin_name%" == "" set plugin_name=plugin_name

:: Remove spaces 
set "plugin_id=%plugin_id: =%"

:intercept_left
if "%plugin_name:~0,1%"==" " set "plugin_name=%plugin_name:~1%"&goto intercept_left

:intercept_right
if "%plugin_name:~-1%"==" " set "plugin_name=%plugin_name:~0,-1%"&goto intercept_right

:: Initialize plugin files
FOR /f "" %%f IN ('dir /b /s src\*.py mcdreforged.plugin.json') do (
    powershell -Command "(gc %%f) -creplace 'plugin_id', '%plugin_id%' | Out-File -encoding ASCII %%f"
    powershell -Command "(gc %%f) -creplace 'plugin_name', '%plugin_name%' | Out-File -encoding ASCII %%f"
)

ren src\plugin_id %plugin_id%

echo Initialization complete for plugin %plugin_name% (%plugin_id%).
del %0