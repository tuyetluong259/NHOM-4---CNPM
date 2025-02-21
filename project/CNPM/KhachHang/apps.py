from django.apps import AppConfig

class KhachHangConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'KhachHang'

    def ready(self):
        import KhachHang.signals  # Kích hoạt signals
