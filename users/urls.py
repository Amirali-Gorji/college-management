from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterUserView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenObtainPairView.as_view(), name='refresh-token'),
    path('register/', RegisterUserView.as_view(), name='register-user'),
]