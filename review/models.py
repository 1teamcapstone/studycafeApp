from datetime import timezone
from django.conf import settings
from django.db import models
from accounts.models import User
from datetime import datetime
from django.urls import reverse

class Review(models.Model):
    contents = models.TextField(verbose_name="내용")
    sca_name= models.CharField(max_length=30, verbose_name="스터디카페") #장소 추가
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name = "등록 시간")
    writer = models.ForeignKey('accounts.User', verbose_name = "작성자", on_delete = models.CASCADE)

    def __str__(self):
        return self.contents
        
    class Meta:
        db_table = "review_comment"
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"


