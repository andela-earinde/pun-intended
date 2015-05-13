from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.core import validators
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password,
                 is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=30,
        help_text='Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.',
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.', 'invalid')
        ], unique=True)
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    description = models.TextField()

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return sel.username

    def get_short_name(self):
        return self.username
    

