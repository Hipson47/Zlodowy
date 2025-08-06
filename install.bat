@echo off
echo =================================================
echo.
echo      INSTALLING DEPENDENCIES FOR ZLODOWY
echo.
echo =================================================

REM --- Backend Dependencies ---
echo.
echo [1/2] Installing backend Python dependencies...
cd backend
if errorlevel 1 (
    echo ERROR: Could not find the 'backend' directory.
    goto :error
)

echo.
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip.
    goto :error
)

echo.
echo Installing requirements from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install backend dependencies.
    goto :error
)
cd ..
echo.
echo Backend dependencies installed successfully.
echo.

REM --- Frontend Dependencies ---
echo [2/2] Installing frontend npm dependencies...
cd frontend
if errorlevel 1 (
    echo ERROR: Could not find the 'frontend' directory.
    goto :error
)

echo.
echo Installing npm packages...
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install frontend dependencies.
    goto :error
)
cd ..
echo.
echo Frontend dependencies installed successfully.
echo.

echo =================================================
echo.
echo      ALL DEPENDENCIES INSTALLED SUCCESSFULLY
echo.
echo =================================================
goto :end

:error
echo.
echo An error occurred. Please check the output above.

:end
pause
