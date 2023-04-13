from django.db import models

# Create your models here.



class OrderCheckoutTasks(models.Model):
    checkoutID = models.CharField(max_length=500)
    execution_time = models.DateTimeField()
    executed = models.BooleanField(default=False)
