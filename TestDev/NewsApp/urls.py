from django.contrib import admin
from django.urls import path
from .views import News,Home

urlpatterns = [
    path('news/', News,name="News"),
path('home/', Home,name="Home"),
path('', Home,name="Home")
]