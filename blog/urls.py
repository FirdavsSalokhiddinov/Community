from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<str:pk>/', views.requested_post, name='requested_post'),
]
