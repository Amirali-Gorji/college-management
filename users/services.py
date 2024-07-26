from users.models import CollegeUser, UserPermission
from django.contrib.auth.models import Permission

class UserService:
    def create_user(username, password, role):
        user = CollegeUser.objects.create_user(username=username, password=password, role=role)
        try:
            model_name = UserPermission._meta.model_name

            if role == "manager" or role == "teacher":
                permissions = Permission.objects.filter(content_type__model=model_name)
                for perm in permissions:
                    user.user_permissions.add(perm)

            elif role == "student":
                allowed_permissions = ["can_view_semester", "can_view_course", "can_view_offer_course",
                                    "can_view_student_class","can_update_student_class",
                                    "can_delete_student_class","can_add_student_class"]
                
                permissions = Permission.objects.filter(content_type__model=model_name, codename__in=allowed_permissions)
                for perm in permissions:
                    user.user_permissions.add(perm)
                    
        except Exception as e:
            CollegeUser.objects.filter(username=username).delete()
            return False, str(e)
        return True, "OK"
