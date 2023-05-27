from django.urls import path, include
from . import views
import review

app_name="review"

urlpatterns = [
    path('list/', views.review_list),
    path('write/', views.review_write),
    
]