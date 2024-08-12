from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import index, MenuItemView, SingleMenuItemView

urlpatterns = [
    path('', index, name='home'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]