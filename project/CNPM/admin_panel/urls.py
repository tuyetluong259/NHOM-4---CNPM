from django.urls import path
from .views import revenue_api

urlpatterns = [
    path('api/revenue/', revenue_api, name='revenue_api'),
]
