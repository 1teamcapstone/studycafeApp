from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    published_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=30)
    study_place = models.CharField(max_length=30)
    study_day = models.CharField(max_length=30)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    limit_people = models.IntegerField(default=2)
    text = models.TextField(default='', blank=True)
    
    def publish(self):
        self.end_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def apply_success(self):
        limit_people = limit_people + 1
        return int(limit_people)
        
        


