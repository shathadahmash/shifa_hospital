from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = "Create default groups and users"

    def handle(self, *args, **kwargs):
        roles = {
            "Admin": {
                "username": "admin",
                "password": "Admin12345",
                "email": "admin@example.com",
                "is_staff": True,
                "is_superuser": True,
            },
            "Receptionist": {
                "username": "receptionist",
                "password": "Reception12345",
                "email": "receptionist@example.com",
                "is_staff": True,
                "is_superuser": False,
            },
            "Doctor": {
                "username": "doctor",
                "password": "Doctor12345",
                "email": "doctor@example.com",
                "is_staff": True,
                "is_superuser": False,
            },
            "Nurse": {
                "username": "nurse",
                "password": "Nurse12345",
                "email": "nurse@example.com",
                "is_staff": True,
                "is_superuser": False,
            },
        }

        for group_name, data in roles.items():
            group, _ = Group.objects.get_or_create(name=group_name)

            user, _ = User.objects.get_or_create(username=data["username"])
            user.email = data["email"]
            user.is_staff = data["is_staff"]
            user.is_superuser = data["is_superuser"]
            user.is_active = True
            user.set_password(data["password"])
            user.save()

            user.groups.clear()
            user.groups.add(group)

            self.stdout.write(
                self.style.SUCCESS(
                    f"{data['username']} user ready in {group_name} group"
                )
            )