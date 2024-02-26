from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)  # Use auto_now_add instead of auto_add_now
    
    def __str__(self):
        return self.title
