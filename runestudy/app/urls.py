from django.urls import path
from app import views


urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('users/', views.userList, name='user-list'),
    path('users/<int:pk>/', views.userDetail, name='user-detail'),
    path('users/create/', views.userCreate, name="user-create"),
    path('users/<int:pk>/update/', views.userUpdate, name='user-update'),
    path('users/<int:pk>/delete/', views.userDelete, name='user-delete'),
]
