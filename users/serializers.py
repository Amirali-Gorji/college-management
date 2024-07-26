from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import CollegeUser
    
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeUser
        fields = '__all__'
