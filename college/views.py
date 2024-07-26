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
from users.permissions import CollegeAuthentication



class SemesterView(ModelViewSet):
    required_permissions = {
        'list': 'can_view_semester',
        'retrieve': 'can_view_semester',
        'update': 'can_update_semester',
        'destroy': 'can_delete_semester',
        'create': 'can_add_semester',
    }
    permission_classes = [CollegeAuthentication]

    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class CourseView(ModelViewSet):
    required_permissions = {
        'list': 'can_view_course',
        'retrieve': 'can_view_course',
        'update': 'can_update_course',
        'destroy': 'can_delete_course',
        'create': 'can_add_course',
    }
    permission_classes = [CollegeAuthentication]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OfferCourseView(ModelViewSet):
    required_permissions = {
        'list': 'can_view_offer_course',
        'retrieve': 'can_view_offer_course',
        'update': 'can_update_offer_course',
        'destroy': 'can_delete_offer_course',
        'create': 'can_add_offer_course',
    }
    permission_classes = [CollegeAuthentication]

    queryset = OfferCourse.objects.all()
    serializer_class = OfferCourseSerializer


class StudentClassView(ModelViewSet):
    required_permissions = {
        'list': 'can_view_student_class',
        'retrieve': 'can_view_student_class',
        'update': 'can_update_student_class',
        'destroy': 'can_delete_student_class',
        'create': 'can_add_student_class',
    }
    permission_classes = [CollegeAuthentication]

    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer
    



