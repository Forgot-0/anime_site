from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
def avatarka_user_path(instance, filename):
    return f'users/{instance.username}/{filename}'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True)
    email = models.EmailField(_('email'), max_length=40, unique=True)
    phone = models.CharField(_('phone number'), max_length=30,\
        null=True, blank=True)
    avatarka = models.ImageField(upload_to=avatarka_user_path, blank=True, null=True)

    date_create = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_verified = models.BooleanField(_('verified'), default=False)

    STATUS_CHOICES = (
    ('S', 'Разработчик'),
    ('A', 'Редактор'),
    ('B', 'Модератор'),
    ('C', 'Премиум'),
    ('D', 'Обычный пользователь'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='D',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def get_full_name(self):
        return self.username

    def __str__(self):
        return str(self.email)

    class Meta:
        unique_together = ('username', 'email', 'phone')
        