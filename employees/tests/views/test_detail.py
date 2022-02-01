import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee


class TestEmployeeDetail(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name='Johnny tester',
            job_title='Software developer',
            birth_date='2004-01-29',
            hire_date='2022-01-29'
        )

    def test_should_return_200(self):
        url = reverse('employee-detail', args=[self.employee.id])
        request = self.client.get(
            url
        )

        assert request.status_code == 200

    def test_should_return_employee_model_fields(self):
        url = reverse('employee-detail', args=[self.employee.id])
        request = self.client.get(
            url
        )

        assert 'name' in request.data
        assert 'job_title' in request.data
        assert 'birth_date' in request.data
        assert 'hire_date' in request.data

    def test_should_return_404_for_employee_not_found(self):
        url = reverse('employee-detail', args=[3])
        request = self.client.get(
            url
        )

        assert request.status_code == 404
