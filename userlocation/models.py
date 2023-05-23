from django.db import models


class UserLocation(models.Model):

    location = models.CharField(max_length=128)



    class Meta:
        db_table = 'user_location'
        verbose_name = '사용자위치'
        verbose_name_plural = '사용자위치'
