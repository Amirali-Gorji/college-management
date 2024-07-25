from rest_framework import serializers

from college.models import (
    Semester,
    Course,
    OfferCourse,
    StudentClass
)

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class OfferCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferCourse
        fields = "__all__"


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = "__all__"
