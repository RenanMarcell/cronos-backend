import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestServiceCreate(APITestCase):
    def test_should_return_200(self):
        url = reverse('service-create')
        request = self.client.post(
            url,
            {
                'name': 'Service for testing package',
                'description': 'All solutions to test your application',
                'price': 9.99
            }
        )

        assert request.status_code == 200

    def test_should_return_service_model_fields(self):
        url = reverse('service-create')
        request = self.client.post(
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
        url = reverse('service-create')
        request = self.client.post(
            url,
            {
                'name': 'Service for testing package',
                'description': 'All solutions to test your application',
                'price': 'de graça'
            }
        )

        assert request.status_code == 400

    def test_should_return_400_for_missing_data(self):
        url = reverse('service-create')
        request = self.client.post(
            url,
            {
                'name': 'Service for testing package',
                'description': 'All solutions to test your application'
            }
        )

        assert request.status_code == 400
