from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import DeliveryPartner, Vehicle
from .serializers import DeliveryPartnerSerializer, VehicleSerializer

class DeliveryPartnerViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPartner.objects.all()
    serializer_class = DeliveryPartnerSerializer
    
    @action(detail=False, methods=['post'])
    def auto_assign(self, request):
        lat = request.data.get('lat')
        lng = request.data.get('lng')
        vehicle_type = request.data.get('vehicle_type')
        
        if not lat or not lng:
            return Response({'error': 'Latitude and longitude required'}, status=status.HTTP_400_BAD_REQUEST)
        
        partners = DeliveryPartner.objects.filter(status='online')
        nearest = None
        min_distance = float('inf')
        
        for partner in partners:
            if partner.latitude and partner.longitude:
                dist = ((float(lat) - float(partner.latitude)) ** 2 + (float(lng) - float(partner.longitude)) ** 2) ** 0.5
                if dist < min_distance and dist <= 10:
                    min_distance = dist
                    nearest = partner
        
        if nearest:
            return Response({
                'partner': DeliveryPartnerSerializer(nearest).data,
                'distance_km': round(min_distance * 111, 2)
            })
        else:
            return Response({'message': 'No available partners nearby'}, status=status.HTTP_404_NOT_FOUND)
