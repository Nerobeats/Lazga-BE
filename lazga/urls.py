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
# password
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentications
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
     # Password-props
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # Items
    path('create/', views.ItemCreateView.as_view(), name='create'),
    path('list/', views.ItemsList.as_view(), name='list'),
    path('update/<int:item_id>', views.ItemUpdateView.as_view(), name='update'),
    path('delete/<int:item_id>', views.DeleteItemView.as_view(), name='delete'),
    # Orders
    path('additem/', views.OrderItemCreateView.as_view(), name='add-item-create'),
    path('submitorder/', views.SubmitOrder.as_view(), name='submit-order-update'),
    # path('create/order/', views.OrderCreateView.as_view(), name='order-create'),
    path('list/orders/', views.OrdersList.as_view(), name='orders-list'),
    path('update/order/<int:order_id>',
         views.OrderUpdateView.as_view(), name='order-update'),
    path('delete/order/<int:orderitem_id>',
         views.OrderItemDeleteView.as_view(), name='order-delete'),
    # Types (Categories)
    path('types/', views.TypesList.as_view(), name='types-list'),
    # Profile
    path('profile/<int:profile_id>/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('profile/addtofavorites/', views.AddToFavorites.as_view(), name='add-to-favorites'),
    path('profile/removefavorite/', views.RemoveFavorite.as_view(), name='remove-favorites'),
   

]
