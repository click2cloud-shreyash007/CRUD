"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

# whenever we add app in our project we need to add it in settings.py file inside INSTALLED_APPS

urlpatterns = [
    path('',views.first),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
]
