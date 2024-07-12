from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, UserImage
from .serializers import UserSerializer, UserImageSerializer
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# This views.py take http requests and return http responses like in HTMl documents


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response(
        {"message": "This is a protected view for authenticated users only."}
    )


# CRUD operation for User model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def like(self, request, pk=None):
        user = self.get_object()
        # Implement your like logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["post"])
    def pass_user(self, request, pk=None):
        user = self.get_object()
        # Implement your pass logic here
        return Response(status=status.HTTP_204_NO_CONTENT)


# CRUD operation for UserImage model.
class UserImageViewSet(viewsets.ModelViewSet):
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer


#Operation for creating new accounts
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data["username"])
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": response.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
