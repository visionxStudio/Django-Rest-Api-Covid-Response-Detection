from django.db import models
import sqlite3, time
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username', primary_key=True)
    Phone_Number = models.CharField(max_length=14, default="")
    DOB = models.DateField()
    Date = models.DateField(default=timezone.now())
    Address = models.CharField(max_length=500)
    Profile_Picture = models.ImageField(default="default.jpg", upload_to='user_pics')
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img1 = Image.open(self.Profile_Picture.path)
        img1.thumbnail((200, 200))
        img1.save(self.Profile_Picture.path)


class hospitalProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='hospital', primary_key=True)
    Phone_Number = models.CharField(max_length=14, default="")
    ESTD = models.DateField()
    Date = models.DateField(default=timezone.now())
    Address = models.CharField(max_length=500)
    Pan_Number=models.CharField(max_length=100,default="")
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -Profile'

