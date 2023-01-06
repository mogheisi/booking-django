from rest_framework import status
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.api.serializers import RegisterSerializer
from users.api.serializers import LoginStep1Serializer, LoginStep2Serializer
from users.models import User


class RegisterApiView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginStep1View(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginStep1Serializer


class LoginStep2View(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LoginStep2Serializer(data=request.data, context={'request': request})
        serializer.is_valid()
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        payload = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(payload)
