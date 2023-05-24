from django.urls import path
from . import views

urlpatterns = [
    path('plz/', views.test_view, name='test_view'),
]