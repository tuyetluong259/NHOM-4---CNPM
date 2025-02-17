from django.urls import path
from .views import revenue_api
from admin_panel.views import revenue_dashboard

urlpatterns = [
    path('api/revenue/', revenue_api, name='revenue_api'),

    path('revenue-dashboard/', revenue_dashboard, name='revenue-dashboard'),
]
