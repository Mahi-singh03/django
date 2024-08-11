from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('menu/', views.MenuView.as_view()),
	path('menu/<int:pk>', views.MenuItemView.as_view()),
	# path('message/', views.msg),
	path('api-token-auth/', obtain_auth_token),
]