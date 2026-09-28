from django.contrib import admin
from .models import StockMovement

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'to_state', 'to_city', 'movement_date', 'status']
    list_filter = ['to_state', 'status', 'transport_type']
    search_fields = ['to_city', 'to_state', 'product__name']
    date_hierarchy = 'movement_date'
