from django.db import models
from django.utils.timezone import now

class SystemConfig(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Revenue(models.Model):
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.date}: {self.amount}"
