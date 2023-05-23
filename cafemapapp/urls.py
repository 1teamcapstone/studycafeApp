from django.urls import path
from . import views

urlpatterns = [
    path('backtest/', views.getTestDatas, name='backtest'),
]