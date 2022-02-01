import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestBlogCreate(APITestCase):
    def test_should_return_200(self):
        url = reverse('blog-create')
        request = self.client.post(
            url,
            {
                'title': 'Test title',
                'category': 'Testing',
                'author': 'John test',
                'content': 'Tests are important'
            }
        )

        assert request.status_code == 200

    def test_should_return_blog_model_fields(self):
        url = reverse('blog-create')
        request = self.client.post(
            url,
            {
                'title': 'Test title',
                'category': 'Testing',
                'author': 'John test',
                'content': 'Tests are important'
            }
        )

        assert 'title' in request.data
        assert 'category' in request.data
        assert 'author' in request.data
        assert 'content' in request.data
        assert 'created_at' in request.data
        assert 'updated_at' in request.data

    def test_should_return_400_for_invalid_data(self):
        url = reverse('blog-create')
        request = self.client.post(
            url,
            {
                'title': 'Test title',
                'category': 'Testing',
                'author': True,
                'content': 'Tests are important'
            }
        )

        assert request.status_code == 400

    def test_should_return_400_for_missing_data(self):
        url = reverse('blog-create')
        request = self.client.post(
            url,
            {
                'title': 'Test title',
                'category': 'Testing',
                'author': 'John test',
            }
        )

        assert request.status_code == 400
