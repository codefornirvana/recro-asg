from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200, null=False, default="anonymous user")
    email = models.EmailField(_('email address'))
    phonenumber = models.CharField(max_length=12, unique=True)
    meta = JSONField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'phonenumber'
    objects = CustomUserManager()

    def __str__(self):
        return self.phonenumber