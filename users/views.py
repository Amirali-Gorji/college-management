from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status

from users.serializers import RegisterUserSerializer
from users.models import CollegeUser
from users.services import UserService


class RegisterUserView(CreateModelMixin, GenericViewSet):
    queryset = CollegeUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.role == 'manager':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                # Creat user
                res_status, msg = UserService.create_user(username=data['username'], password=data['password'], role=data['role'])
                
                # Return error if process is unsuccessful
                if not res_status:
                    return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)
                # Success message
                return Response(status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"error": "Unauthorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)


