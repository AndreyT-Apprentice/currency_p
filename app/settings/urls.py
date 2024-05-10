"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from currency.views import (
    contact_us_create,
    generate_password,
    rate_create, rate_delete, rate_details, rate_list, rate_update,
    soucre_create,
    source_delete,
    source_list,
    source_update, sourse_details
    )

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('gen-pass/', generate_password),
    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/source/list/', source_list),
    path('currency/source/details/<int:pk>/', sourse_details),
    path('currency/rate/create/', rate_create),
    path('currency/rate/update/<int:pk>/', rate_update),
    path('currency/rate/delete/<int:pk>/', rate_delete),
    path('currency/contact_us/create/', contact_us_create),
    path('currency/source/create/', soucre_create),
    path('currency/source/update/<int:pk>/', source_update),
    path('currency/source/delete/<int:pk>/', source_delete),
]
