from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer


@api_view(['GET'])
def blogsList(request):
    blogs = Blog.objects.all().order_by('-id')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={
        200: BlogSerializer,
        404: 'Not Found',
    }
)
@api_view(['GET'])
def blogDetail(request, id):
    try:
        blogs = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(
            'Blog not found!',
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = BlogSerializer(blogs, many=False)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=BlogSerializer,
    responses={
        200: BlogSerializer,
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def blogsCreate(request):
    serializer = BlogSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@swagger_auto_schema(
    method='put',
    request_body=BlogSerializer,
    responses={
        200: BlogSerializer,
        400: 'Bad Request',
    }
)
@api_view(['PUT'])
def blogUpdate(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(
            'Blog not found!',
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = BlogSerializer(instance=blog, data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@swagger_auto_schema(
    method='delete',
    responses={
        200: 'Blog deleted!',
        404: 'Not Found',
    }
)
@api_view(['DELETE'])
def blogDelete(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(
            'Blog not found!',
            status=status.HTTP_404_NOT_FOUND
        )

    blog.delete()

    return Response('Blog deleted!')
