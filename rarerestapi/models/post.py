from django.db import models
from platformdirs import user_log_dir
from rarerestapi.models.category import Category
from rarerestapi.models.rare_user import RareUser

class Post(models.Model):
    
    user = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    image_url = models.CharField(max_length=1000)
    content = models.CharField(max_length=300)
    approved = models.BooleanField()