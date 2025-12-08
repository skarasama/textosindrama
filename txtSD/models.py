from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, nomUsuario, correoElectronico, password=None, **extra_fields):
        if not nomUsuario:
            raise ValueError("El usuario debe tener un nombre de usuario.")
        if not correoElectronico:
            raise ValueError("El usuario debe tener un correo electrónico.")
        user = self.model(
            nomUsuario=nomUsuario,
            correoElectronico=self.normalize_email(correoElectronico),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nomUsuario, correoElectronico, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nomUsuario, correoElectronico, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nomUsuario = models.CharField(max_length=150, unique=True)
    correoElectronico = models.EmailField(max_length=255, unique=True)
    nivelEducativo = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nomUsuario'
    REQUIRED_FIELDS = ['correoElectronico']

    def __str__(self):
        return self.nomUsuario






