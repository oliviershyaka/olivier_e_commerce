from django.shortcuts import redirect, render
from django.http import HttpResponse

from e_commerceApp.forms import AddProductForm, RegisterForm
from e_commerceApp.models import OurProduct


def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form saved successfully!")
            return redirect('registration_success')
        else:
            print("Form has errors:", form.errors)
    else:
        form = RegisterForm()
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