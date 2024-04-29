from django.urls import path
from .views import map

urlpatterns = [
    path('map/', map, name='map'),
]