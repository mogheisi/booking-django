from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.api.views import RegisterApiView
from .views import LoginStep1View, LoginStep2View


urlpatterns = [
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login-step-one/', LoginStep1View.as_view(), name='step-one'),
    path('login-step-two/', LoginStep2View.as_view(), name='step-two'),
]
