from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import *


# Create your models here.

class Account(AbstractBaseUser):
    username=None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email= models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=14)

    is_verified = models.BooleanField(default=False)
    last_login_time = models.DateField(null=True, blank=True)
    last_logout_time = models.DateField(null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


