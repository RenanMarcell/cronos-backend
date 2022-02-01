import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee


class TestEmployeeUpdate(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name='Johnny NOT tester',
            job_title='Not software developer',
            birth_date='2004-01-23',
            hire_date='2022-01-21'
        )

    def test_should_return_200_and_update_model(self):
        assert Employee.objects.first().name == 'Johnny NOT tester'

        url = reverse('employee-update', args=[self.employee.id])
        request = self.client.put(
            url,
            {
                'name': 'Johnny tester',
                'job_title': 'Software developer',
                'birth_date': '2004-01-29',
                'hire_date': '2022-01-29'
            }
        )
        updated_employee = Employee.objects.first()

        assert request.status_code == 200
        assert updated_employee.name == 'Johnny tester'
        assert updated_employee.job_title == 'Software developer'
        assert updated_employee.birth_date.isoformat() == '2004-01-29'
        assert updated_employee.hire_date.isoformat() == '2022-01-29'

    def test_should_return_employee_model_fields(self):
        url = reverse('employee-update', args=[self.employee.id])
        request = self.client.put(
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
        url = reverse('employee-update', args=[self.employee.id])
        request = self.client.put(
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
        url = reverse('employee-update', args=[self.employee.id])
        request = self.client.put(
            url,
            {
                'name': 'Johnny tester',
                'job_title': 'Software developer',
                'birth_date': '2004-01-29'
            }
        )

        assert request.status_code == 400
