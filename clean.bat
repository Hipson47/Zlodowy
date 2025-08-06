@echo off
echo =================================================
echo.
echo           CLEANING ZLODOWY PROJECT
echo.
echo =================================================

REM --- Clean Backend ---
echo.
echo [1/3] Cleaning backend...
cd backend
if errorlevel 1 (
    echo WARNING: Could not find the 'backend' directory.
    goto :skip_backend
)

echo Deleting __pycache__ directories...
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        echo rmdir /s /q "%%d"
        rmdir /s /q "%%d"
    )
)

echo Deleting .pyc files...
del /s /q *.pyc

cd ..
echo Backend cleaned.
echo.

:skip_backend

REM --- Clean Frontend ---
echo [2/3] Cleaning frontend...
cd frontend
if errorlevel 1 (
    echo WARNING: Could not find the 'frontend' directory.
    goto :skip_frontend
)

if exist "node_modules" (
    echo Removing node_modules directory...
    rmdir /s /q node_modules
)
cd ..
echo Frontend cleaned.
echo.

:skip_frontend

REM --- Clean Docker ---
echo [3/3] Cleaning Docker...
echo Stopping and removing containers...
docker-compose down
echo.
echo Pruning Docker system...
docker system prune -f
echo.
echo Docker cleaned.
echo.

echo =================================================
echo.
echo         CLEANUP COMPLETED SUCCESSFULLY
echo.
echo =================================================

pause
