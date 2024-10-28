from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    USER_TYPES = (
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),  # New user type option
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    # contact_number = models.CharField(max_length=15)  # Optional contact number field
    additional_info = models.TextField(blank=True)  # Optional field for extra info

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"



