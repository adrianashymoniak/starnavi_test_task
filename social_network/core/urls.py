from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    path('posts/', views.PostsList.as_view()),
    path('posts/<int:pk>/', views.PostsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
