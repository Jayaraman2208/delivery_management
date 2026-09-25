from django.db import models
from warehouses.models import Warehouse
from inventory.models import Product
from orders.models import Order
from fleet.models import DeliveryPartner

class StockMovement(models.Model):
    MOVEMENT_TYPES = (
        ('warehouse_to_customer', 'Warehouse to Customer'),
        ('warehouse_to_warehouse', 'Warehouse to Warehouse'),
        ('supplier_to_warehouse', 'Supplier to Warehouse'),
        ('return', 'Return'),
    )
    TRANSPORT_TYPES = (
        ('lorry', 'Lorry'),
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('train', 'Train'),
        ('ship', 'Ship'),
        ('air', 'Air'),
        ('other', 'Other'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='stock_movements')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_movements')
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='outgoing_movements')
    to_latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    to_longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    to_city = models.CharField(max_length=100)
    to_state = models.CharField(max_length=100)
    to_district = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=30, choices=MOVEMENT_TYPES, default='warehouse_to_customer')
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_TYPES)
    delivery_partner = models.ForeignKey(DeliveryPartner, on_delete=models.SET_NULL, null=True, related_name='stock_movements')
    batch_number = models.CharField(max_length=50, blank=True)
    tracking_number = models.CharField(max_length=100, blank=True)
    movement_date = models.DateTimeField(auto_now_add=True)
    delivered_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='in_transit')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['to_state', 'movement_date']),
            models.Index(fields=['to_city', 'movement_date']),
        ]

    def __str__(self):
        return f'{self.product.name} - {self.quantity} to {self.to_city} ({self.movement_date})'
