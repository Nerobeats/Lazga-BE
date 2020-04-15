"""lazga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView
from lazga_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create/', views.ItemCreateView.as_view(), name='create'),
    path('list/', views.ItemsList.as_view(), name='list'),
    path('detail/<int:item_id>', views.ItemDetailView.as_view(), name='detail'),
    path('update/<int:item_id>', views.ItemUpdateView.as_view(), name='update'),
    path('delete/<int:item_id>', views.DeleteView.as_view(), name='delete'),
]

#####
# Alternative (easier to understand) URLS
#####

alt_urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('items/', views.ItemsView.as_view(), name='list-create'),
    path('items/<int:item_id>', views.ItemView.as_view(), name='detail'),
]
