@echo off
echo =================================================
echo.
echo           RUNNING LINTERS FOR ZLODOWY
echo.
echo =================================================

REM --- Backend Linting ---
echo.
echo [1/2] Linting backend Python code...
cd backend
if errorlevel 1 (
    echo ERROR: Could not find the 'backend' directory.
    goto :error
)

echo.
echo Running flake8...
flake8 app/ tests/
if errorlevel 1 (
    echo ERROR: flake8 found issues.
    goto :error
)

echo.
echo Running mypy...
mypy app/ --ignore-missing-imports
if errorlevel 1 (
    echo ERROR: mypy found type errors.
    goto :error
)

cd ..
echo.
echo Backend linting passed.
echo.


REM --- Frontend Linting ---
echo [2/2] Linting frontend TypeScript code...
cd frontend
if errorlevel 1 (
    echo ERROR: Could not find the 'frontend' directory.
    goto :error
)

echo.
echo Running ESLint...
call npm run lint
if errorlevel 1 (
    echo ERROR: ESLint found issues.
    goto :error
)
cd ..
echo.
echo Frontend linting passed.
echo.

echo =================================================
echo.
echo      LINTING COMPLETED SUCCESSFULLY
echo.
echo =================================================
goto :end

:error
echo.
echo An error occurred. Please check the output above.

:end
pause
