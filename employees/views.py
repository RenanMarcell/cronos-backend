from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET'])
def employeesList(request):
    employees = Employee.objects.all().order_by('-id')
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='get',
    responses={
        200: EmployeeSerializer,
        404: 'Not Found',
    }
)
@api_view(['GET'])
def employeeDetail(request, id):
    try:
        employees = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(
            'Employee not found!',
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = EmployeeSerializer(employees, many=False)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=EmployeeSerializer,
    responses={
        200: EmployeeSerializer,
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def employeesCreate(request):
    serializer = EmployeeSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@swagger_auto_schema(
    method='put',
    request_body=EmployeeSerializer,
    responses={
        200: EmployeeSerializer,
        400: 'Bad Request',
    }
)
@api_view(['PUT'])
def employeeUpdate(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(
            'Employee not found!',
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = EmployeeSerializer(instance=employee, data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@swagger_auto_schema(
    method='delete',
    responses={
        200: 'Employee deleted!',
        404: 'Not Found',
    }
)
@api_view(['DELETE'])
def employeeDelete(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(
            'Employee not found!',
            status=status.HTTP_404_NOT_FOUND
        )

    employee.delete()

    return Response('Employee deleted!')
