from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin

from django.utils import timezone



class CustomUserManager(BaseUserManager):
    """ 
    Administrador de modelo de usuario personalizado donde el Numero de telefono
    es el identificador único para la autenticación en lugar de los nombres de usuario 
    """ 

    def create_user(self, control, password, **extra_fields):
        if not control:
            raise ValueError(('Escriba un numero control(NUMERO DE CONTROL)'))
        
        control = self.normalize_email(control)
        user = self.model(control=control)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, control, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(control, password, **extra_fields)



class NewUser(AbstractUser):
    
    control       = models.CharField('Numero de Control', max_length=8,unique=True, null=False)
    
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'control'

    # requerido para superuser
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuario'


    def __str__(self):
        return self.control