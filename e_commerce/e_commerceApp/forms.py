from django import forms
from .models import OurProduct, Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'user_name',
            'email',
            'phone_number',
            'company_name',
            'sector',
            'cell',
            'village',
            'nearest_infrastructure',
            'password',
            'user_role',
            'profile_image',
        ]



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
