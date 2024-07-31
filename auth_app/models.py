from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    mobileno = models.CharField(("Mobile Number"), max_length=50)
    nationality = models.CharField(("Nationality"), max_length=50,blank=True)
    gender = models.CharField(("Gender"), max_length=50,blank=True)
    profile = models.ImageField(("Profile"), upload_to='user/profile',default='assets/images/profile_blank.png')