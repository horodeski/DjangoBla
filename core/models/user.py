from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, name=None, description=None, usuario=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")

        alphanumeric = RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')
        if usuario:
            alphanumeric(usuario)

        user = self.model(email=self.normalize_email(email), name=name, description=description, usuario=usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name=None, description=None, usuario=None):
        user = self.create_user(email, password, name=name, description=description, usuario=usuario)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    usuario = models.CharField(max_length=255, blank=True, null=True, validators=[RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')])  # Adicionando campo de usuário com validação
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
