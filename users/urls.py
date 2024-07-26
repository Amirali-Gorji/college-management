from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import SimpleRouter
from users.views import RegisterUserView

router = SimpleRouter()
router.register(r'register', RegisterUserView, basename='register-user')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),

] + router.urls