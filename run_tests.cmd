@echo off
setlocal
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

set "MODE=%~1"
if "%MODE%"=="" set "MODE=all"

if /I "%MODE%"=="unit" (
    set "RC=0"
    if exist "tests\test_redact.py" (
        python -m unittest tests\test_redact.py -v
        if errorlevel 1 exit /b 1
    )
    if exist "tests\test_denylist.py" (
        python -m unittest tests\test_denylist.py -v
        if errorlevel 1 exit /b 1
    )
    if exist "tests\test_shard.py" (
        python -m unittest tests\test_shard.py -v
        if errorlevel 1 exit /b 1
    )
    echo [run_tests.cmd] unit OK
    exit /b 0
)

if /I "%MODE%"=="all" (
    if exist "tests" (
        python -m unittest discover -s tests -p "test_*.py" -v
        if errorlevel 1 exit /b 1
    )
    if exist "tools\verify_no_secrets.py" (
        python tools\verify_no_secrets.py
        if errorlevel 1 exit /b 1
    )
    echo [run_tests.cmd] all OK
    exit /b 0
)

echo Unknown mode: %MODE% (expected: unit or all)
exit /b 2

