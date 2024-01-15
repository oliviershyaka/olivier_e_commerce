from multiprocessing import AuthenticationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from e_commerceApp.forms import AddProductForm, RegistrationForm
from e_commerceApp.models import Account, OurProduct
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
import json

def base_view(request):
    form = AuthenticationForm()  # Instantiate the form
    return render(request, 'more/main.html', {'form': form})

def admin(request):
    if request.user.is_authenticated and request.user.account.user_role == 1:
        return render(request, 'homepage/admindashboard.html')
    else:
        messages.error(request, 'You are unauthorized to access the admin dashboard.')
        return redirect('base')

def clientdashord(request):
    return render(request, 'homepage/clientdashord.html')

def about_view(request):
    return render(request, 'more/about.html')

def contactUs_view(request):
    return render(request, 'more/contactus.html')

def new_product_view(request):
    return render(request, 'new_product.html')

def register_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            account = Account.objects.create(
                user=user,
                address_id=form.cleaned_data['address_id'],
                phone_number=form.cleaned_data['phone_number'],
                company_name=form.cleaned_data['company_name'],
                user_role=form.cleaned_data['user_role'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                gender=form.cleaned_data['gender'],
                profile_image=form.cleaned_data['profile_image'],
            )
            auth_login(request, user)  

            if account.user_role == 1:
                messages.success(request, 'Registration successful as role 1. You are now logged in.')
                return redirect('adminDashboard')
            elif account.user_role == 2:
                messages.success(request, 'Registration successful as role 2. You are now logged in.')
                return redirect('clientdashord')
            else:
                messages.error(request, 'Invalid user_role.')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    return render(request, 'auntatication/register_modal.html', {'form': form,})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                if user.account.user_role == 1:
                    messages.success(request, 'Login successful as role 1.')
                    return redirect('adminDashboard')
                elif user.account.user_role == 2:
                    messages.success(request, 'Login successful as role 2.')
                    return redirect('clientdashord')
                else:
                    messages.error(request, 'Invalid role.')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = AuthenticationForm()

    return render(request, 'auntatication/login_modal.html', {'form': form})



def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            product_instance = form.save()
            # You can perform additional actions here if needed
            return redirect('base') 
    else:
        form = AddProductForm()

    return render(request, 'more/New_product.html', {'form': form})

def login_viewyy(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.account.user_role == 1:
                messages.success(request, 'Login successful as role 1.')
                return redirect('adminDashboard')
            elif user.account.user_role == 2:
                messages.success(request, 'Login successful as role 2.')
                return redirect('clientdashord')
            else:
                messages.error(request, 'Invalid role.')

        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'auntatication/login_modal')




def list_of_product_view(request):
    products = OurProduct.objects.all()  
    return render(request, 'more/listofproduct.html', {'products': products})