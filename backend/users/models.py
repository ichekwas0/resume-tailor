from django.db import models

# Create your models here.
from django.db import models
from .usermanager import MyUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid 


# Create your models here.
class MyUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField('Email', primary_key=True, unique=True, blank=False, max_length=150)
    first_name = models.CharField('First Name', max_length=150, blank=True)
    last_name = models.CharField('Last Name', max_length=150, blank=True)
    resume = models.FileField(upload_to="files/", max_length=100)
    
    is_active = models.BooleanField("is_active", default=True)
    is_staff = models.BooleanField('is_active', default=False)
    
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email