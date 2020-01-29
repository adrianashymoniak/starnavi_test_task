from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    path('posts/', views.PostsList.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostsDetail.as_view()),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
