from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView

from users.api.serializers import RegisterSerializer


class RegisterApiView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
