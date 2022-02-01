from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.blogsList, name='blogs-list'),
    path('<str:id>/detail/', views.blogDetail, name='blog-detail'),
    path('create/', views.blogsCreate, name='blog-create'),
    path('<str:id>/update/', views.blogUpdate, name='blog-update'),
    path('<str:id>/delete/', views.blogDelete, name='blog-delete'),
]
