import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestEmployeeCreate(APITestCase):
    def test_should_return_200(self):
        url = reverse('employee-create')
        request = self.client.post(
            url,
            {
                'name': 'Johnny tester',
                'job_title': 'Software developer',
                'birth_date': '2004-01-29',
                'hire_date': '2022-01-29'
            }
        )

        assert request.status_code == 200

    def test_should_return_employee_model_fields(self):
        url = reverse('employee-create')
        request = self.client.post(
            url,
            {
                'name': 'Johnny tester',
                'job_title': 'Software developer',
                'birth_date': '2004-01-29',
                'hire_date': '2022-01-29'
            }
        )

        assert 'name' in request.data
        assert 'job_title' in request.data
        assert 'birth_date' in request.data
        assert 'hire_date' in request.data

    def test_should_return_400_for_invalid_data(self):
        url = reverse('employee-create')
        request = self.client.post(
            url,
            {
                'name': 'Johnny tester',
                'job_title': 'Software developer',
                'birth_date': '2020-01-29',
                'hire_date': '2022-01-29'
            }
        )

        assert request.status_code == 400

    def test_should_return_400_for_missing_data(self):
        url = reverse('employee-create')
        request = self.client.post(
            url,
            {
                'name': 'Johnny tester',
                'job_title': 'Software developer',
                'hire_date': '2022-01-29'
            }
        )

        assert request.status_code == 400
