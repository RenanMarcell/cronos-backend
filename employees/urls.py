from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.employeesList, name="employees-list"),
    path('<str:id>/detail/', views.employeeDetail, name="employee-detail"),
    path('create/', views.employeesCreate, name="employees-create"),
    path('<str:id>/update/', views.employeeUpdate, name="employee-update"),
    path('<str:id>/delete/', views.employeeDelete, name="employee-delete"),
]
