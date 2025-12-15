from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view, name='home'),  # Коли шлях порожній, викликаємо simple_view
]