from celery import shared_task
from django.db.models import Sum
from datetime import datetime, timedelta
from .models import StockMovement

@shared_task
def update_dashboard_metrics():
    from analytics.models import DashboardMetric
    from django.db.models import Count
    
    # Update daily metrics
    today = datetime.now().date()
    
    # Total deliveries by state
    state_wise = StockMovement.objects.filter(
        status='delivered',
        movement_date__date=today
    ).values('to_state').annotate(
        total=Sum('quantity'),
        count=Count('id')
    )
    
    for data in state_wise:
        DashboardMetric.objects.update_or_create(
            metric_type='total_deliveries',
            date=today,
            state=data['to_state'],
            defaults={'value': data['total']}
        )
    
    return f"Updated metrics for {today}"

@shared_task
def send_delivery_notification(order_id):
    from notifications.models import Notification
    from orders.models import Order
    
    order = Order.objects.get(id=order_id)
    Notification.objects.create(
        user=order.customer,
        notification_type='delivery_assignment',
        title='Order Out for Delivery',
        message=f'Your order #{order.order_number} is out for delivery!',
        data={'order_id': order.id}
    )
    return f"Notification sent for order {order_id}"
