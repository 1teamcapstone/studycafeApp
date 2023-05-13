from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64)
    useremail = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
    location = models.CharField(max_length=128, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'cafeProject_user'
        verbose_name = '카페앱 사용자'
        verbose_name_plural = '카페앱 사용자'
