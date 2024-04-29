from django.urls import path
from .views import mapping_view

urlpatterns = [
    path('', mapping_view, name='mapping'),
]