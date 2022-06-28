from django.db import models
from rarerestapi.models.post import Post
from rarerestapi.models.rare_user import RareUser

class Comment(models.Model):
    
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=False, auto_now_add=False)
    content = models.CharField(max_length=150)