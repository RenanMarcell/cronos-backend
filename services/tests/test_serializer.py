import pytest
from datetime import date
from rest_framework.exceptions import ValidationError

from services.serializers import ServiceSerializer


class TestServiceSerializer:
    def test_should_serialize_data(self):
        data = {
            'name': 'Service for testing package',
            'description': 'All solutions to test your application',
            'price': 9.99
        }

        try:
            assert ServiceSerializer(data=data).is_valid(raise_exception=True)
        except Exception as e:
            pytest.fail('It should not have raised: {}'.format(e))

    @pytest.mark.parametrize('price', [
        0,
        -0.1,
        -1000
    ])
    def test_should_raise_validation_error_for_invalid_birth_date(self, price):
        data = {
            'name': 'Service for testing package',
            'description': 'All solutions to test your application',
            'price': price
        }

        with pytest.raises(ValidationError):
            ServiceSerializer(data=data).is_valid(raise_exception=True)
