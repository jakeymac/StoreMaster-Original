from django.urls import path

from . import views

app_name = "Stores"

urlpatterns = [
    path('stores', views.index,name='index'),
]