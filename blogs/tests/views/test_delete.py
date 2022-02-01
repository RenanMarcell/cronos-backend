import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blogs.models import Blog


class TestBlogDelete(APITestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title='Test not title',
            category='Not testing',
            author='John not test',
            content='Tests are not important'
        )

    def test_should_return_200(self):
        url = reverse('blog-delete', args=[self.blog.id])
        request = self.client.delete(url)

        assert request.status_code == 200

    def test_should_return_confirmation_of_blog_deleted(self):
        url = reverse('blog-delete', args=[self.blog.id])
        request = self.client.delete(url)

        assert request.data == 'Blog deleted!'

    def test_should_return_404_for_blog_not_found(self):
        url = reverse('blog-delete', args=[3])
        request = self.client.delete(url)
        assert request.status_code == 404
