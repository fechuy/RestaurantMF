"""papeleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [    
    path('', views.user_logout, name='logout'),    
    path('registro/', views.registro, name='registro'),
    path('login/', views.user_login, name='login'),
    path('listaReservacion/', views.verReservacionListView.as_view(), name='listaReservacion'),
    #path('reservacion/', views.reservacionesCreateView.as_view(), name='reservacion')
]