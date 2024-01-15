from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path("", views.index, name="home"),
    path("login", views.login, name="login"),
    path('registration_success/', views.registration_success, name='registration_success'),
    path("ourproduct", views.add_product, name="product"),
    path('logout/',LogoutView.as_view(), name='logout'),
]