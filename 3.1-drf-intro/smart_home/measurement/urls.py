from django.urls import path
from django.contrib import admin
from .views import SensorCreateView, MakeMeasurement, OneSensor

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('measurements/', MakeMeasurement.as_view()),
    path('sensors/<int:pk>/', OneSensor.as_view())

]
