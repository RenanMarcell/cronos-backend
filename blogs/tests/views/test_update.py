import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blogs.models import Blog


class TestBlogUpdate(APITestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title='Test not title',
            category='Not testing',
            author='John not test',
            content='Tests are not important'
        )

    def test_should_return_200_and_update_model(self):
        assert Blog.objects.first().title == 'Test not title'

        url = reverse('blog-update', args=[self.blog.id])
        request = self.client.put(
            url,
            {
                'title': 'Test title',
                'category': 'Testing',
                'author': 'John test',
                'content': 'Tests are important'
            }
        )
        updated_blog = Blog.objects.first()

        assert request.status_code == 200
        assert updated_blog.title == 'Test title'
        assert updated_blog.category == 'Testing'
        assert updated_blog.author == 'John test'
        assert updated_blog.content == 'Tests are important'

    def test_should_return_blog_model_fields(self):
        url = reverse('blog-update', args=[self.blog.id])
        request = self.client.put(
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
        url = reverse('blog-update', args=[self.blog.id])
        request = self.client.put(
            url,
            {
                'title': 'Test title',
                'category': 'Testing',
                'author': False,
                'content': 'Tests are important'
            }
        )

        assert request.status_code == 400

    def test_should_return_400_for_missing_data(self):
        url = reverse('blog-update', args=[self.blog.id])
        request = self.client.put(
            url,
            {
                'title': 'Test title',
                'category': 'Testing',
                'author': 'John test'
            }
        )

        assert request.status_code == 400
