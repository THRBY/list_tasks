from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_verified = models.BooleanField('verified', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.email

class Task(models.Model):
    ID = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    deadline = models.DateTimeField(auto_now=False, blank=True, null=False)
    performed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title