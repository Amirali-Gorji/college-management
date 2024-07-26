from django.db import models
from django.contrib.auth.models import AbstractUser


class UserPermission(models.Model):
    class Meta:
        permissions = (
            # college
            ("can_view_semester", "can view semester"),
            ("can_update_semester", "can update semester"),
            ("can_delete_semester", "can delete semester"),
            ("can_add_semester", "can add semester"),
            ("can_view_course", "can view course"),
            ("can_update_course", "can update course"),
            ("can_delete_course", "can delete course"),
            ("can_add_course", "can add course"),
            ("can_view_offer_course", "can view offer course"),
            ("can_update_offer_course", "can update offer course"),
            ("can_delete_offer_course", "can delete offer course"),
            ("can_add_offer_course", "can add offer course"),
            ("can_view_student_class", "can view student class"),
            ("can_update_student_class", "can update student class"),
            ("can_delete_student_class", "can delete student class"),
            ("can_add_student_class", "can add student class"),   
        )


class CollegeUser(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)




