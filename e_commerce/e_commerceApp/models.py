from django.db import models
from django.contrib.auth.models import User


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



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    user_role = models.IntegerField(default=2, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    def _str_(self):
        return str(self.user.id)