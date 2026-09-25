# Run this script to start the backend
# Setup Database First

Write-Host "Starting Delivery Management Backend..." -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan

# Activate virtual environment
.\venv\Scripts\activate

# Make migrations
Write-Host "
[1/4] Creating migrations..." -ForegroundColor Green
python manage.py makemigrations

# Apply migrations
Write-Host "
[2/4] Applying migrations..." -ForegroundColor Green
python manage.py migrate

# Create superuser
Write-Host "
[3/4] Creating superuser..." -ForegroundColor Green
python manage.py createsuperuser

# Start server
Write-Host "
[4/4] Starting development server..." -ForegroundColor Green
Write-Host "Server will run at: http://localhost:8000" -ForegroundColor Yellow
Write-Host "Admin panel: http://localhost:8000/admin" -ForegroundColor Yellow
python manage.py runserver 0.0.0.0:8000
