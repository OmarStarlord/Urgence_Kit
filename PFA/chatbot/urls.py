from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.chatbot, name='chatbot_home'),
    # Add more URL patterns for other chatbot-related views if needed
]
