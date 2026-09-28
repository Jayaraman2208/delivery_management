@echo off
echo =========================================
echo   DELIVERY MANAGEMENT SYSTEM BACKEND
echo =========================================
echo.
echo Starting the backend server...
echo.
call venv\Scripts\activate
python manage.py runserver 0.0.0.0:8000
pause
