from django.urls import path
from django.contrib import admin
from .views import SensorView

urlpatterns = [
    path('sensors/', SensorView.as_view())
]
