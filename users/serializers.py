from rest_framework import serializers

from users.models import CollegeUser

class RegisterUserSerializer(serializers.Serializer):
    class Meta:
        model = CollegeUser
        fields = '__all__'
