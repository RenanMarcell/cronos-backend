import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee


class TestEmployeeList(APITestCase):
    def setUp(self):
        Employee.objects.bulk_create([
            Employee(
                name='Johnny tester',
                job_title='Software developer',
                birth_date='2004-01-29',
                hire_date='2022-01-29'
            ),
            Employee(
                name='Johnny tester',
                job_title='Software developer',
                birth_date='2004-01-29',
                hire_date='2022-01-29'
            ),
            Employee(
                name='Johnny tester',
                job_title='Software developer',
                birth_date='2004-01-29',
                hire_date='2022-01-29'
            ),
        ])

    def test_should_return_200(self):
        url = reverse('employees-list')
        request = self.client.get(url)

        assert request.status_code == 200

    def test_should_return_a_array(self):
        url = reverse('employees-list')
        request = self.client.get(url)

        assert isinstance(request.data, list)
        assert len(request.data) == 3

    def test_should_return_employee_model_fields(self):
        url = reverse('employees-list')
        request = self.client.get(url)

        assert 'name' in request.data[0]
        assert 'job_title' in request.data[0]
        assert 'birth_date' in request.data[0]
        assert 'hire_date' in request.data[0]
