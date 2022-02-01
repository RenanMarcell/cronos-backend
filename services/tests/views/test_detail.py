import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from services.models import Service


class TestServiceDetail(APITestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name='Service for testing package',
            description='All solutions to test your application',
            price=9.99
        )

    def test_should_return_200(self):
        url = reverse('service-detail', args=[self.service.id])
        request = self.client.get(
            url
        )

        assert request.status_code == 200

    def test_should_return_service_model_fields(self):
        url = reverse('service-detail', args=[self.service.id])
        request = self.client.get(
            url
        )

        assert 'name' in request.data
        assert 'description' in request.data
        assert 'price' in request.data
        assert 'created_at' in request.data

    def test_should_return_404_for_service_not_found(self):
        url = reverse('service-detail', args=[3])
        request = self.client.get(
            url
        )

        assert request.status_code == 404
