from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_vist = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    def __str__(self):
     return f"{self.name} ({self.lists.count()} lists)"


class Lists(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_vist = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE , related_name='lists')
    def __str__(self):
        return self.name
    
