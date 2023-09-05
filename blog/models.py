from django.db import models

# Create your models here.
from accounts.models import CustomUser

class Blog(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)