from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name=models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name

class UserPersona(models.Model):
    birthday=models.DateField(null=True, blank=True)
    def bday(self):
        return self.birthday
    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    age=property(age)

class UserProfile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    last_name=models.CharField(max_length=100)
    first_name= models.CharField(max_length=100)
    country= models.CharField(max_length=50)
    interests= models.ManyToManyField(UserInterest, blank=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)

