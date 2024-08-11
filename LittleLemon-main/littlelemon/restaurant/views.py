from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import decorators
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
def index(request):
	return render(request, 'index.html', {})


class MenuView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	

class MenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

# @decorators.api_view()
# @decorators.permission_classes([permissions.IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	# permission_classes = [permissions.IsAuthenticated]

# @decorators.api_view()
# @decorators.permission_classes([permissions.IsAuthenticated])
# # @authentication_classes([TokenAuthentication])
# def msg(request):
# 	return Response({"message":"This view is protected"})