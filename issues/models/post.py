from django.db import models 
from django.contrib.auth.models import User
from issues.models import Category
from datetime import datetime

class Post(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, null=True)
    body = models.TextField(null=False, blank=False)
    number_of_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.body

