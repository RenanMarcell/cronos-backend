import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from services.models import Service


class TestServiceDelete(APITestCase):
    def setUp(self):
        self.service = Service.objects.create(
            name='Service for testing package',
            description='All solutions to test your application',
            price=9.99
        )

    def test_should_return_200(self):
        url = reverse('service-delete', args=[self.service.id])
        request = self.client.delete(url)

        assert request.status_code == 200

    def test_should_return_confirmation_of_service_deleted(self):
        url = reverse('service-delete', args=[self.service.id])
        request = self.client.delete(url)

        assert request.data == 'Service deleted!'

    def test_should_return_404_for_service_not_found(self):
        url = reverse('service-delete', args=[3])
        request = self.client.delete(url)
        assert request.status_code == 404
