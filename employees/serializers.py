from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'

	def validate_hire_date(self, date):
		today = date.today()

		if date > today:
			raise ValidationError('This date should not be a future date')
		return date

	def validate_birth_date(self, date):
		today = date.today()

		eighteen_birthday = date + relativedelta(years=18)
		if eighteen_birthday > today:
			raise ValidationError('Employee must be over 18')
		return date
