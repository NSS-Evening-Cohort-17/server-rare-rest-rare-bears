from django.db import models
from django.contrib.auth.models import User

class RareUser(models.Model):

    bio = models.CharField(max_length=50)
    profile_image_url = models.CharField(max_length=1000)
    create_on = models.DateField(auto_now=True)
    active = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)