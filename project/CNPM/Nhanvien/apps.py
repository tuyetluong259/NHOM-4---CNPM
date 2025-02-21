from django.apps import AppConfig

class NhanvienConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Nhanvien'

    def ready(self):
        import Nhanvien.signals  # Kích hoạt signals
