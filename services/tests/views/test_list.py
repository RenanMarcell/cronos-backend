import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from services.models import Service


class TestServiceList(APITestCase):
    def setUp(self):
        Service.objects.bulk_create([
            Service(
                name='Service for testing package',
                description='All solutions to test your application',
                price=9.99
            ),
            Service(
                name='Service for testing package',
                description='All solutions to test your application',
                price=9.99
            ),
            Service(
                name='Service for testing package',
                description='All solutions to test your application',
                price=9.99
            ),
        ])

    def test_should_return_200(self):
        url = reverse('services-list')
        request = self.client.get(url)

        assert request.status_code == 200

    def test_should_return_a_array(self):
        url = reverse('services-list')
        request = self.client.get(url)

        assert isinstance(request.data, list)
        assert len(request.data) == 3

    def test_should_return_service_model_fields(self):
        url = reverse('services-list')
        request = self.client.get(url)

        assert 'name' in request.data[0]
        assert 'description' in request.data[0]
        assert 'price' in request.data[0]
        assert 'created_at' in request.data[0]
