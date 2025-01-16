from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class Category(models.Model):
    sub_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='sub_categories',  # Thêm related_name để tránh xung đột
        null=True,
        blank=True
    )
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

# Sau đó định nghĩa Customer
class Customer(models.Model):
    category = models.ManyToManyField(Category, related_name='customers')
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=False
    )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
