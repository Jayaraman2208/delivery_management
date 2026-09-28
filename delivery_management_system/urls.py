from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter

# Import your API viewsets
from stock_movement.views import StockMovementViewSet
from fleet.views import DeliveryPartnerViewSet

# Optional: import other app URLs (uncomment if they exist)
# from orders.urls import urlpatterns as orders_urls
# from accounts.urls import urlpatterns as accounts_urls


def home(request):
    """
    Simple homepage to avoid 404 on the root URL.
    """
    return JsonResponse({
        "status": "ok",
        "message": "Delivery Management API is running",
        "endpoints": [
            "/admin/",
            "/api/",
            "/api/stock-movements/",
            "/api/delivery-partners/",
        ]
    })


# DRF router — registers your viewsets under /api/
router = DefaultRouter()
router.register(r'stock-movements', StockMovementViewSet)
router.register(r'delivery-partners', DeliveryPartnerViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # If your apps have their own urls.py files, uncomment these:
    # path('api/orders/', include('orders.urls')),
    # path('api/accounts/', include('accounts.urls')),
]