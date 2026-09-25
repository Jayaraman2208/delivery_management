from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock_movement.views import StockMovementViewSet
from fleet.views import DeliveryPartnerViewSet

router = DefaultRouter()
router.register(r'stock-movements', StockMovementViewSet)
router.register(r'delivery-partners', DeliveryPartnerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
