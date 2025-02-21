from django.apps import AppConfig

class BacsiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bacsi'

    def ready(self):
        import Bacsi.signals
