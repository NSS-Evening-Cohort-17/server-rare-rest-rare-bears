from django.db import models
from rarerestapi.models.rare_user import RareUser

class Subscription(models.Model):

    follower = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='follower')
    author = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='author')
    created_on = models.DateField(auto_now=False, auto_now_add=False)
    ended_on = models.DateField(auto_now=False, auto_now_add=False)