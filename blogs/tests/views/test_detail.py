import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blogs.models import Blog


class TestBlogDetail(APITestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title='Test title',
            category='Testing',
            author='John test',
            content='Tests are important'
        )

    def test_should_return_200(self):
        url = reverse('blog-detail', args=[self.blog.id])
        request = self.client.get(
            url
        )

        assert request.status_code == 200

    def test_should_return_blog_model_fields(self):
        url = reverse('blog-detail', args=[self.blog.id])
        request = self.client.get(
            url
        )

        assert 'title' in request.data
        assert 'category' in request.data
        assert 'author' in request.data
        assert 'content' in request.data
        assert 'created_at' in request.data
        assert 'updated_at' in request.data

    def test_should_return_404_for_blog_not_found(self):
        url = reverse('blog-detail', args=[3])
        request = self.client.get(
            url
        )

        assert request.status_code == 404
