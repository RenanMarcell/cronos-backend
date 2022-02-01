import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee


class TestEmployeeDelete(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name='Johnny tester',
            job_title='Software developer',
            birth_date='2004-01-29',
            hire_date='2022-01-29'
        )

    def test_should_return_200(self):
        url = reverse('employee-delete', args=[self.employee.id])
        request = self.client.delete(url)

        assert request.status_code == 200

    def test_should_return_confirmation_of_employee_deleted(self):
        url = reverse('employee-delete', args=[self.employee.id])
        request = self.client.delete(url)

        assert request.data == 'Employee deleted!'

    def test_should_return_404_for_employee_not_found(self):
        url = reverse('employee-delete', args=[3])
        request = self.client.delete(url)
        assert request.status_code == 404
