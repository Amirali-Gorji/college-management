
from django.urls import path
from rest_framework.routers import SimpleRouter

from college.views import (
    SemesterView,
    CourseView,
    OfferCourseView,
    StudentClassView,
)

router = SimpleRouter()
router.register(r'semester', SemesterView, basename='semester')
router.register(r'course', CourseView, basename='course')
router.register(r'offer-course', OfferCourseView, basename='offer-course')
router.register(r'student-class', StudentClassView, basename='student-class')

urlpatterns = [

] + router.urls