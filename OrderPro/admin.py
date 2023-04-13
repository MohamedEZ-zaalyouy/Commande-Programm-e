from django.contrib import admin
from .models import OrderCheckoutTasks 
# Register your models here.


class OrderCheckoutTasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'checkoutID', 'execution_time', 'executed']

admin.site.register(OrderCheckoutTasks, OrderCheckoutTasksAdmin)
