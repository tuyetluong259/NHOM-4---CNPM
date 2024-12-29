from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # Sử dụng TemplateView cho trang chủ nếu cần

urlpatterns = [
    path('admin/', admin.site.urls),
    path('QLC/', include('QLC.urls')),  # Bao gồm các URL từ ứng dụng QLC
    path('', TemplateView.as_view(template_name="room_list.html"), name="home"),  # Trang chủ
]
