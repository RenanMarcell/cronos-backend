from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Service
from .serializers import ServiceSerializer


@api_view(['GET'])
def servicesList(request):
    services = Service.objects.all().order_by('-id')
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={
        200: ServiceSerializer,
        404: 'Not Found',
    }
)
@api_view(['GET'])
def serviceDetail(request, id):
    try:
        services = Service.objects.get(id=id)
    except Service.DoesNotExist:
        return Response(
            'Service not found!',
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ServiceSerializer(services, many=False)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=ServiceSerializer,
    responses={
        200: ServiceSerializer,
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def servicesCreate(request):
    serializer = ServiceSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@swagger_auto_schema(
    method='put',
    request_body=ServiceSerializer,
    responses={
        200: ServiceSerializer,
        400: 'Bad Request',
    }
)
@api_view(['PUT'])
def serviceUpdate(request, id):
    try:
        service = Service.objects.get(id=id)
    except Service.DoesNotExist:
        return Response(
            'Service not found!',
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = ServiceSerializer(instance=service, data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@swagger_auto_schema(
    method='delete',
    responses={
        200: 'Service deleted!',
        404: 'Not Found',
    }
)
@api_view(['DELETE'])
def serviceDelete(request, id):
    try:
        service = Service.objects.get(id=id)
    except Service.DoesNotExist:
        return Response(
            'Service not found!',
            status=status.HTTP_404_NOT_FOUND
        )
    service.delete()

    return Response('Service deleted!')
