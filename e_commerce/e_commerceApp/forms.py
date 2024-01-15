from django import forms
from .models import OurProduct
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class AddProductForm(forms.ModelForm):
    class Meta:
        model = OurProduct
        fields = [
            'product_name',
            'product_description',
            'product_price',
            'product_discount',
            'product_image',
            'product_status',
        ]


class RegistrationForm(UserCreationForm):
    address_id = forms.IntegerField(required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    company_name = forms.CharField(max_length=100, required=False)
    user_role = forms.IntegerField(initial=2, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    gender = forms.CharField(max_length=6, widget=forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')]))
    profile_image = forms.ImageField(required=False,)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address_id', 'phone_number', 'company_name', 'user_role', 'first_name', 'last_name', 'gender','profile_image']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken.')
        return username