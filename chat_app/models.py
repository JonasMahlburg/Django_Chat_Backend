from django.db import models

# Create your models here.
class Chat(models.Model):
    name= models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)    