from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('history/', views.chat_history_view, name='chat_history'),
    # Add more paths as needed for other views
]
