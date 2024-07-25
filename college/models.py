from django.db import models
from django.contrib.auth.models import AbstractUser


class CollegeUser(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Semester(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()


class Course(models.Model):
    name = models.CharField(max_length=100)


class OfferCourse(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher = models.ForeignKey(CollegeUser, on_delete=models.PROTECT)
    desc = models.TextField()

    class Meta:
        unique_together = ('semester', 'course', 'teacher')


class StudentClass(models.Model):
    offer_course = models.ForeignKey(OfferCourse, on_delete=models.CASCADE)
    student = models.ForeignKey(CollegeUser, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('offer_course', 'student')

    