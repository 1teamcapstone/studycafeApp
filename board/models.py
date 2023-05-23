from django.db import models
from accounts.models import User
class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name = "등록 시간")
    writer = models.ForeignKey('accounts.User', verbose_name = "작성자", on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "community_board"
        verbose_name = "게시물"
        verbose_name_plural = "게시물"
        

# Create your models here.
