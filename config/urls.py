"""
URL configuration for config project.

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
from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("", app.views.root, name="root"),
    path("hey-name/", app.views.hey_name, name ="hey_name"),
    path("future-age/", app.views.how_old, name="future_age"),
    path("order-total/", app.views.order_total, name="order_total"),
    path("cb1/", app.views.near_hundred, name="cb1"),
    path("cb2/", app.views.stringsplosion, name="cb2"),
    path("cb3/", app.views.catdog, name="cb3"),
    path("cb4", app.views.lone_sum, name="cb4"),
    path('admin/', admin.site.urls),
]
