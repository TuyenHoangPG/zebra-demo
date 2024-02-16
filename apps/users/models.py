from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from common.const import UserRole
from common.model import TimeStampMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("Missing email!")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("role", UserRole.ADMIN)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, TimeStampMixin):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(choices=UserRole.choices, default=UserRole.USER)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    def __str__(self):
        return self.email

    def is_exist(user_id):
        try:
            user = User.objects.get(pk=user_id)
            return True
        except User.DoesNotExist:
            return False

    class Meta:
        db_table = "users"
