
from django.contrib import admin
from django.urls import path, include
from .api import CreateOrderFromCheckout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/create_order", CreateOrderFromCheckout.as_view()),
]
