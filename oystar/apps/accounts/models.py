from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
from django.forms.fields import CharField
from django.utils.translation import gettext as _
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, full_name, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, full_name, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, full_name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    full_name = CharField(max_length = 100)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    @property
    def get_full_name(self) :
        return self.full_name

# class UserInterest(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#     normalized_name=models.CharField(max_length=64, unique=True)
#     def __str__(self):
#         return self.name

# class UserPersona(models.Model):
#     birthday=models.DateField(null=True, blank=True)
#     def bday(self):
#         return self.birthday
#     def age(self):
#         import datetime
#         return int((datetime.date.today() - self.birthday).days / 365.25  )
#     age=property(age)

# class UserProfile(models.Model):
#     user =models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
#     bio = models.CharField(max_length=500, blank=True, null=True)
#     website = models.URLField(max_length=200, blank=True, null=True)
#     last_name=models.CharField(max_length=100)
#     first_name= models.CharField(max_length=100)
#     country= models.CharField(max_length=50)
#     interests= models.ManyToManyField(UserInterest, blank=True)
#     persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)

