from django.urls import path, include
from . import views
import review

app_name="review"

urlpatterns = [
    path('list/<int:pk>/', views.review_list),
    path('write/<int:pk>/', views.review_write),
]