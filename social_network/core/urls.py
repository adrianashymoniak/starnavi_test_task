from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from core.views import LoginView, RegisterUsersView, LogoutView, PostsList, \
    PostsDetail, api_root, PostLikeAPIToggle

urlpatterns = [
    path('posts/', PostsList.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostsDetail.as_view()),
    path('post/<int:pk>/like/', PostLikeAPIToggle.as_view(),
         name='post-detail'),
    path('', api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/register/', RegisterUsersView.as_view(), name='auth-register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
