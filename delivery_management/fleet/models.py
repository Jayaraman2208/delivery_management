from django.db import models
from accounts.models import User

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('2-wheeler', '2-Wheeler'),
        ('3-wheeler', '3-Wheeler'),
        ('4-wheeler', '4-Wheeler'),
        ('truck', 'Truck'),
    )
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    registration_number = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField(help_text='Capacity in kg')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.registration_number} ({self.vehicle_type})'

class DeliveryPartner(models.Model):
    STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('busy', 'Busy'),
        ('on_delivery', 'On Delivery'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_profile')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, related_name='partners')
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='offline')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_deliveries = models.IntegerField(default=0)
    average_delivery_time = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    vehicle_documents = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.status}'
