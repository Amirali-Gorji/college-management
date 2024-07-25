from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from college.models import (
    Semester,
    Course,
    OfferCourse,
    StudentClass,
)
from college.serializers import (
    SemesterSerializer,
    CourseSerializer,
    OfferCourseSerializer,
    StudentClassSerializer,
)


class UserCreateView(APIView):
    # TODO: endpoint for superuser to create teacher and student
    def post(self, request, *args, **kwargs):
        pass


class SemesterView(ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OfferCourseView(ModelViewSet):
    queryset = OfferCourse.objects.all()
    serializer_class = OfferCourseSerializer


class StudentClassView(ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer


class StudentView(ModelViewSet):
    pass
    # queryset = User.obj



