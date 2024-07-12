# users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView
from .views import UserViewSet, UserListView
from .views import protected_view


from .views import UserImageViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"images", UserImageViewSet)

urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="register"),
    path("", UserListView.as_view(), name="user-list"),  # List users at /api/users/
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/protected/", protected_view, name="protected"),
    path("api/", include(router.urls)),
]
