@echo off
echo =================================================
echo.
echo             RUNNING TESTS FOR ZLODOWY
echo.
echo =================================================

REM --- Backend Tests ---
echo.
echo [1/2] Running backend Python tests...
cd backend
if errorlevel 1 (
    echo ERROR: Could not find the 'backend' directory.
    goto :error
)

echo.
echo Running pytest...
pytest
if errorlevel 1 (
    echo ERROR: Pytest encountered errors.
    goto :error
)
cd ..
echo.
echo Backend tests passed successfully.
echo.


REM --- Frontend Tests ---
echo [2/2] Running frontend TypeScript tests...
cd frontend
if errorlevel 1 (
    echo ERROR: Could not find the 'frontend' directory.
    goto :error
)

echo.
echo Running Jest tests...
call npm test
if errorlevel 1 (
    echo ERROR: Jest tests failed.
    goto :error
)
cd ..
echo.
echo Frontend tests passed successfully.
echo.

echo =================================================
echo.
echo         ALL TESTS PASSED SUCCESSFULLY
echo.
echo =================================================
goto :end

:error
echo.
echo Tests failed. Please check the output above.

:end
pause
