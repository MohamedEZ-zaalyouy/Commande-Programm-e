from celery import shared_task
from django.utils import timezone
from .models import OrderCheckoutTasks
from . import views


@shared_task
def execute_CreateOrderFromCheckout():
    
    now = timezone.now()
    print("im her,", now)

    objects_to_execute = OrderCheckoutTasks.objects.filter(execution_time__lte=now, executed=False)
    for obj in objects_to_execute:

        # Call your Post API function here
        CreateOrderPro = views.CreateOrderProFromCheckout(obj.checkoutID)

        obj.executed = True
        obj.save()
