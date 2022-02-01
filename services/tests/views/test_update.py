from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from services.models import Service


class TestServiceUpdate(APITestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name='Against test service',
            description='Just deploy on production',
            price=18.99
        )

    def test_should_return_200_and_update_model(self):
        assert Service.objects.first().name == 'Against test service'

        url = reverse('service-update', args=[self.service.id])
        request = self.client.put(
            url,
            {
                'name': 'Service for testing package',
                'description': 'All solutions to test your application',
                'price': 9.99
            }
        )
        updated_service = Service.objects.first()

        assert request.status_code == 200
        assert updated_service.name == 'Service for testing package'
        assert updated_service.description == (
            'All solutions to test your application'
        )
        assert updated_service.price == Decimal('9.99')

    def test_should_return_service_model_fields(self):
        url = reverse('service-update', args=[self.service.id])
        request = self.client.put(
            url,
            {
                'name': 'Service for testing package',
                'description': 'All solutions to test your application',
                'price': 9.99
            }
        )

        assert 'name' in request.data
        assert 'description' in request.data
        assert 'price' in request.data
        assert 'created_at' in request.data

    def test_should_return_400_for_invalid_data(self):
        url = reverse('service-update', args=[self.service.id])
        request = self.client.put(
            url,
            {
                'name': 'Service for testing package',
                'description': 'All solutions to test your application',
                'price': 'de graça'
            }
        )

        assert request.status_code == 400

    def test_should_return_400_for_missing_data(self):
        url = reverse('service-update', args=[self.service.id])
        request = self.client.put(
            url,
            {
                'name': 'Service for testing package',
                'description': 'All solutions to test your application'
            }
        )

        assert request.status_code == 400
