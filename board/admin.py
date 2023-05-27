from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', )

admin.site.register(Board, BoardAdmin)

admin.site.register(Comment)


# Register your models here.
