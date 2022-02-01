import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blogs.models import Blog


class TestBlogList(APITestCase):
    def setUp(self):
        Blog.objects.bulk_create([
            Blog(
                title='Test title',
                category='Testing',
                author='John test',
                content='Tests are important'
            ),
            Blog(
                title='Test title',
                category='Testing',
                author='John test',
                content='Tests are important'
            ),
            Blog(
                title='Test title',
                category='Testing',
                author='John test',
                content='Tests are important'
            ),
        ])

    def test_should_return_200(self):
        url = reverse('blogs-list')
        request = self.client.get(url)

        assert request.status_code == 200

    def test_should_return_a_array(self):
        url = reverse('blogs-list')
        request = self.client.get(url)

        assert isinstance(request.data, list)
        assert len(request.data) == 3

    def test_should_return_blog_model_fields(self):
        url = reverse('blogs-list')
        request = self.client.get(url)

        assert 'title' in request.data[0]
        assert 'category' in request.data[0]
        assert 'author' in request.data[0]
        assert 'content' in request.data[0]
        assert 'created_at' in request.data[0]
        assert 'updated_at' in request.data[0]
