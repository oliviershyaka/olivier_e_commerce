from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from e_commerceApp.forms import AddProductForm, RegistrationForm
from e_commerceApp.models import Account, OurProduct
from django.contrib.auth import authenticate, login as auth_login

def index(request):
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
            auth_login(request, user)  # Use auth_login instead of login

            if account.user_role == 1:
                messages.success(request, 'Registration successful as role 1. You are now logged in.')
                return redirect('home')
            elif account.user_role == 2:
                messages.success(request, 'Registration successful as role 2. You are now logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid user_role.')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')

    products = OurProduct.objects.all()
    return render(request, 'home.html', {'form': form, 'products': products})

def login(request):
    return HttpResponse("login")


def registration_success(request):
    return render(request, 'registration_success.html')





def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            product_instance = form.save()
            # You can perform additional actions here if needed
            return redirect('home') 
    else:
        form = AddProductForm()

    return render(request, 'our_product.html', {'form': form})



def login_view(request):
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

    return render(request, 'login.html')