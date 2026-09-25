from django.contrib.auth import get_user_model
from warehouses.models import Warehouse
from inventory.models import Product, Category
from fleet.models import Vehicle, DeliveryPartner
from django.contrib.gis.geos import Point

User = get_user_model()

# Create admin if not exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@geologix.com', 'admin123')

# Create warehouses
warehouses = [
    {'name': 'Central Warehouse', 'code': 'CW001', 'city': 'Chennai', 'state': 'Tamil Nadu', 'lat': 13.0827, 'lng': 80.2707},
    {'name': 'South Distribution', 'code': 'SD002', 'city': 'Chennai', 'state': 'Tamil Nadu', 'lat': 12.9775, 'lng': 80.2203},
    {'name': 'West Logistics Hub', 'code': 'WL003', 'city': 'Chennai', 'state': 'Tamil Nadu', 'lat': 13.0986, 'lng': 80.1591},
]

for w in warehouses:
    Warehouse.objects.get_or_create(
        code=w['code'],
        defaults={
            'name': w['name'],
            'address': f'{w["city"]}, {w["state"]}',
            'location': Point(w['lng'], w['lat']),
            'city': w['city'],
            'state': w['state'],
            'capacity': 1000,
            'is_active': True
        }
    )

# Create categories
categories = ['Food Supplies', 'Medical Supplies', 'Emergency Equipment', 'Construction Materials']
for cat in categories:
    Category.objects.get_or_create(name=cat)

print('✅ Initial data created successfully!')
