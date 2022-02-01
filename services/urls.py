from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.servicesList, name="services-list"),
    path('<str:id>/detail/', views.serviceDetail, name="service-detail"),
    path('create/', views.servicesCreate, name="service-create"),
    path('<str:id>/update/', views.serviceUpdate, name="service-update"),
    path('<str:id>/delete/', views.serviceDelete, name="service-delete"),
]
