from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('users/', views.userList, name='user-list'),
    path('users/<int:pk>/', views.userDetail, name='user-detail'),
    path('users/create/', views.userCreate, name="user-create"),
    path('users/<int:pk>/update/', views.userUpdate, name='user-update'),
    path('users/<int:pk>/delete/', views.userDelete, name='user-delete'),
    path('skills/', views.skillList, name='skill-list'),
    path('skills/<int:pk>/', views.skillDetail, name='skill-detail'),
    path('skills/create/', views.skillCreate, name="skill-create"),
    path('skills/<int:pk>/update/', views.skillUpdate, name='skill-update'),
    path('skills/<int:pk>/delete/', views.skillDelete, name='skill-delete'),
]
