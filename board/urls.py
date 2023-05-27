from django.urls import path, include
from . import views
import board

app_name="board"

urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>/', views.board_detail),
    path('comment/create/',views.comment_create_ajax, name="comment_create_ajax"),

    
]