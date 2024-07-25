from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin


from users.serializers import RegisterUserSerializer
from users.models import CollegeUser


class RegisterUserView(GenericViewSet, CreateModelMixin):
    queryset = CollegeUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = []


