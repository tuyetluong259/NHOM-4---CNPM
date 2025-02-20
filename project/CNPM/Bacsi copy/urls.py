from django.urls import path
from . import views  

urlpatterns = [
     path('', views.home, name='home'),
    path('list/', views.list_Bacsi, name='list_Bacsi'),
    path('<int:record_id>/', views.Bacsi_detail, name='Bacsi_detail'),
    path('create/', views.create_Bacsi, name='create_Bacsi'),
    path('<int:record_id>/update/', views.update_Bacsi, name='update_Bacsi'),
    path('<int:record_id>/delete/', views.delete_Bacsi, name='delete_Bacsi'),
    path('medical_records/', views.medical_records, name='medical_records'),
    path('inpatient_care/', views.inpatient_care, name='inpatient_care'),
    path('<int:record_id>/edit_medical/', views.edit_medical, name='edit_medical'),
    path('<int:record_id>/delete_medical/', views.delete_medical, name='delete_medical'),
    path('login/', views.login_view, name='login'),
]
