from django.urls import path

from . import views

app_name = "Accounts"

urlpatterns = [
    path('accounts', views.index,name='index'),
]