from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('about/', views.about_view, name='about'),
    path('new_product/', views.new_product_view, name='new_product'),
    path('list_of_products/', views.list_of_product_view, name='list_of_products'),
    path("adminDashboard", views.admin, name="adminDashboard"),
    path("clientdashord", views.clientdashord, name="clientdashord"),
    
    
    # path("", views.index, name="home"),
    path("login", views.login_view, name="login"),
    path("newUser", views.register_view, name="newUser"),
    
    path("NewProduct", views.add_product, name="product"),
    path("AboutUs", views.about_view, name="AboutUs"),
    path("contactUs", views.contactUs_view, name="contactUs"),
    
    path('logout/',LogoutView.as_view(), name='logout'),
]