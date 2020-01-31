from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView
from core import views
from core.views import LoginView, RegisterUsersView

urlpatterns = [
    path('posts/', views.PostsList.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostsDetail.as_view()),
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/register/', RegisterUsersView.as_view(), name='auth-register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
