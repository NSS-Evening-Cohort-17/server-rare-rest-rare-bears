from django.db import models
from rarerestapi.models.rare_user import RareUser

class DemotionQueue(models.Model):

    action = models.CharField(max_length=150)
    admin = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='admin')
    approver_one = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='approver_on_id')