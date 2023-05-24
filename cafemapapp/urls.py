from django.urls import path
from . import views

urlpatterns = [
    #path('backtest/', views.getTestDatas, name='backtest'),
    path('post/', views.post_view, name='post_view'),
    #path('plz/', views.test_view, name='test_view'),
]