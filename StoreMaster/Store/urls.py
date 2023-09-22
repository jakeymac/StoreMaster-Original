from django.urls import path

from . import views

app_name = "Store"

urlpatterns = [
    path("", views.login_registration_page,name="login_registration_page"),
    path("store", views.store_home, name="store_home"),
    path("register_user",views.register_user, name="register_user"),
    path("register_store",views.register_store,name="register_store"),
    path("login",views.login_user,name="login"),
    path("login_success",views.login_success,name="login_success"),
    
]