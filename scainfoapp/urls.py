from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.test_view, name='test_view'),
    path('hashtag/', views.hashtag_view, name='hashtag'),
    path('has_sort_star/', views.hashtag_view, name='has_sort_star'),
    path('has_sort_review/', views.hashtag_view, name='review'),
    path('sort_star/', views.sortstar_view, name='sort_star'),
    path('sort_review/', views.sortreview_view, name='sort_review'),
    path('like/', views.like_view, name='like_view'),
    path('detail/<int:pk>/', views.sca_detail, name='sca_detail'),
    #path('hashtag/result_sort_star/', views.searchsort_view, name='searchsort'),
    #path('room/', views.room_view, name='hashtag'),
]