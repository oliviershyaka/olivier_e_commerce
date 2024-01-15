from django.db import models


class Register(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(max_length=10)  
    company_name = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    nearest_infrastructure = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=255, default="user", blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user_name


# Create your models here.
from django.db import models

class OurProduct(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.product_name


