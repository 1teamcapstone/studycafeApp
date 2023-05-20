from django.urls import path
from .views import location

app_name="userlocation"

urlpatterns = [
    path('write/', location, name='location'),
   
]