from django.urls import path
from .views import RegisterView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from clubs.views import UserSearchView
from .views import CustomTokenObtainPairView , ProfilePictureView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('upload-pp/', ProfilePictureView.as_view(), name='upload-profile_picture'),
]
