from rest_framework import serializers
from .models import *

class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = ['id', 'title', 'price', 'inventory']
		extra_kwargs = {}

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'