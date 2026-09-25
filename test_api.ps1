# API Test Script
# Run this after starting the server

 = "http://localhost:8000/api"

Write-Host "Testing Stock Movement API..." -ForegroundColor Yellow

# Test 1: Get stock movements
Write-Host "
[1] Getting stock movements..." -ForegroundColor Green
 = Invoke-RestMethod -Uri "/stock-movements/" -Method Get
 | ConvertTo-Json -Depth 3

# Test 2: Get dashboard stats
Write-Host "
[2] Getting dashboard statistics..." -ForegroundColor Green
 = Invoke-RestMethod -Uri "/stock-movements/dashboard_stats/" -Method Get
 | ConvertTo-Json -Depth 3

# Test 3: Test delivery partner auto-assign
Write-Host "
[3] Testing delivery partner auto-assign..." -ForegroundColor Green
 = @{
    lat = 26.8467
    lng = 80.9462
    vehicle_type = "2-wheeler"
} | ConvertTo-Json

 = Invoke-RestMethod -Uri "/delivery-partners/auto_assign/" -Method Post -Body  -ContentType "application/json"
 | ConvertTo-Json -Depth 3

Write-Host "
API Testing Complete!" -ForegroundColor Green
