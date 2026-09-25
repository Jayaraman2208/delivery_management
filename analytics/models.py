from django.db import models
from warehouses.models import Warehouse

class DashboardMetric(models.Model):
    METRIC_TYPES = (
        ('total_orders', 'Total Orders'),
        ('total_deliveries', 'Total Deliveries'),
        ('revenue', 'Revenue'),
        ('delivery_time', 'Average Delivery Time'),
        ('partner_performance', 'Partner Performance'),
    )
    metric_type = models.CharField(max_length=30, choices=METRIC_TYPES)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['metric_type', 'date']),
            models.Index(fields=['state', 'metric_type']),
        ]

    def __str__(self):
        return f'{self.metric_type} - {self.value} ({self.date})'
