"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from autorizaciones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('afiliado/list',views.afiliado_list, name="afiliado_list"),
    path('pedido/list',views.pedido_list, name="pedido_list"),
    path('practica/list',views.practica_list, name="practica_list"),
    path('afiliado/create',views.afiliado_create, name="afiliado_create"),
    path('pedido/create',views.pedido_create, name="pedido_create"),
    path('practica/create',views.practica_create, name="practica_create"),
    path('buscar/', views.buscar_afiliado, name='buscar_afiliado'),
    
]
