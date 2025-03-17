from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import helikopteri_list, helikopteri_specific  # Import the API view



urlpatterns = [
    path('helikopteri/', helikopteri_list),    # URL for fetching JSON data
    path('helikopteri/<pk>/', helikopteri_specific),
]
