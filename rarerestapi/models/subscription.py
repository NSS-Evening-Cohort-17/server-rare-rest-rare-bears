from django.db import models
from rarerestapi.models.rare_user import RareUser

class Subscription(models.Model):
    
    follower_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=False, auto_now_add=False)
    ended_on = models.DateField(auto_now=False, auto_now_add=False)