from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="home"),
    path("login", views.login, name="login"),
    path('registration_success/', views.registration_success, name='registration_success'),
    path("ourproduct", views.add_product, name="product"),
]