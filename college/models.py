from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import CollegeUser

class Semester(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()


class Course(models.Model):
    name = models.CharField(max_length=100)
    unit = models.IntegerField()


class OfferCourse(models.Model):
    class_status_choices = (
        ('active', 'Active'),
        ('deactive', 'Deactive'),
    )
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher = models.ForeignKey(CollegeUser, on_delete=models.PROTECT)
    class_status = models.CharField(choices=class_status_choices, max_length=100)
    desc = models.TextField()

    class Meta:
        unique_together = ('semester', 'course', 'teacher')


class StudentClass(models.Model):
    offer_course = models.ForeignKey(OfferCourse, on_delete=models.CASCADE)
    student = models.ForeignKey(CollegeUser, on_delete=models.PROTECT)
    rate = models.CharField(max_length=10)

    class Meta:
        unique_together = ('offer_course', 'student')





    