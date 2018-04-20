from django.db import models
from django.contrib.auth.models import Group

from users.models import DefaultUser

# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(to=DefaultUser, on_delete=models.SET_NULL, null=True)
    visible_to = models.ManyToManyField(to=Group)