from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'

	def validate_price(self, price):
		if price <= 0:
			raise ValidationError('Price cant be 0 or negative')
		return price
