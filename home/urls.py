# External Imports
from django.contrib import admin
from django.urls import path

# Internal Imports
from . import views

urlpatterns = [
    path('', views.index, name='home')
]