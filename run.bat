@echo off
echo =================================================
echo.
echo      STARTING ZLODOWY WITH DOCKER COMPOSE
echo.
echo =================================================

REM Check if Docker is running
docker-compose ps >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker does not seem to be running.
    echo Please start Docker and try again.
    goto :error
)

echo.
echo Building and running services...
docker-compose up --build
if errorlevel 1 (
    echo ERROR: Docker Compose failed to start.
    goto :error
)

echo.
echo Zlodowy is running.
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:8000
echo.

goto :end

:error
echo.
echo An error occurred. Please check the output above.

:end
pause
