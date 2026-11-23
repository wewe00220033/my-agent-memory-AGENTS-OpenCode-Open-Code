@echo off
setlocal
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

set "MODE=%~1"
if "%MODE%"=="" set "MODE=all"

if /I "%MODE%"=="unit" goto :mode_unit
if /I "%MODE%"=="all" goto :mode_all

echo Unknown mode: %MODE% (expected: unit or all)
endlocal & exit /b 2

:mode_unit
if exist "tests\test_redact.py" (
    python -m unittest tests\test_redact.py -v
    if errorlevel 1 goto :fail
)
if exist "tests\test_denylist.py" (
    python -m unittest tests\test_denylist.py -v
    if errorlevel 1 goto :fail
)
if exist "tests\test_shard.py" (
    python -m unittest tests\test_shard.py -v
    if errorlevel 1 goto :fail
)
if exist "tests\test_snapshot_db.py" (
    python -m unittest tests\test_snapshot_db.py -v
    if errorlevel 1 goto :fail
)
echo [run_tests.cmd] unit OK
endlocal & exit /b 0

:mode_all
if exist "tests" (
    python -m unittest discover -s tests -p "test_*.py" -v
    if errorlevel 1 goto :fail
)
if exist "tools\verify_no_secrets.py" (
    python tools\verify_no_secrets.py
    if errorlevel 1 goto :fail
)
echo [run_tests.cmd] all OK
endlocal & exit /b 0

:fail
endlocal & exit /b 1

