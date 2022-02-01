import pytest
from datetime import date
from rest_framework.exceptions import ValidationError

from employees.serializers import EmployeeSerializer


class TestEmployeeSerializer:
    def test_should_serialize_data(self):
        data = {
            'name': 'Johnny tester',
            'job_title': 'Software developer',
            'birth_date': '2004-01-29',
            'hire_date': '2022-01-29'
        }

        try:
            assert EmployeeSerializer(data=data).is_valid(raise_exception=True)
        except Exception as e:
            pytest.fail('It should not have raised: {}'.format(e))

    def test_should_raise_validation_error_for_invalid_birth_date(self):
        data = {
            'name': 'Johnny tester',
            'job_title': 'Software developer',
            'birth_date': '3000-01-29',
            'hire_date': '2022-01-29'
        }

        with pytest.raises(ValidationError):
            EmployeeSerializer(data=data).is_valid(raise_exception=True)

    def test_should_raise_validation_error_for_invalid_hire_date(self):
        data = {
            'name': 'Johnny tester',
            'job_title': 'Software developer',
            'birth_date': '1999-01-29',
            'hire_date': '3000-01-29'
        }

        with pytest.raises(ValidationError):
            EmployeeSerializer(data=data).is_valid(raise_exception=True)
