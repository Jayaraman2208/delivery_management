from rest_framework import serializers
from .models import DeliveryPartner, Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DeliveryPartnerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    phone = serializers.CharField(source='user.phone', read_only=True)
    
    class Meta:
        model = DeliveryPartner
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
