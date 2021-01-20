from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomGroups(models.Model):
    group_name = models.CharField(max_length=80, unique=True)
    company_name = models.CharField(max_length=80)
    date_created = models.DateField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.date_created = timezone.now()
        return super().save(*args, **kwargs)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    group = models.ForeignKey(CustomGroups, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(blank=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    objects = CustomUserManager()

    def __str__(self):
        return self.email