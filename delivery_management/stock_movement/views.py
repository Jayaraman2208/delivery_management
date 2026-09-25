from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import StockMovement
from .serializers import StockMovementSerializer

class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all().order_by('-movement_date')
    serializer_class = StockMovementSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['to_state', 'to_city', 'product__name']
    ordering_fields = ['movement_date', 'quantity']
    
    @action(detail=False, methods=['get'])
    def state_wise_summary(self, request):
        state = request.query_params.get('state')
        month = request.query_params.get('month')
        
        queryset = self.queryset
        if state:
            queryset = queryset.filter(to_state=state)
        if month:
            queryset = queryset.filter(movement_date__month=month)
            
        summary = queryset.values('to_state', 'product__name').annotate(
            total_quantity=Sum('quantity'),
            total_orders=Count('order', distinct=True)
        )
        return Response(summary)
    
    @action(detail=False, methods=['get'])
    def dashboard_stats(self, request):
        total_delivered = self.queryset.filter(status='delivered').aggregate(
            total=Sum('quantity')
        )['total'] or 0
        
        state_wise = self.queryset.values('to_state').annotate(
            total=Sum('quantity')
        ).order_by('-total')
        
        return Response({
            'total_delivered': total_delivered,
            'state_wise': state_wise,
            'recent_movements': StockMovementSerializer(self.queryset[:10], many=True).data
        })
