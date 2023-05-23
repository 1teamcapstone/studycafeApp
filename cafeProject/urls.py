"""
URL configuration for firstdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views
# from userlocation import views
import cafemapapp.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home), ## 홈화면 주소들은 따로 html끼리모으고..연동시키기
    path('userlocation/', include('userlocation.urls')),
    path('board/', include('board.urls')),
    path('map/',cafemapapp.views.map, name='map'),
    path('study/',cafemapapp.views.study, name='study'),
    path('test/',cafemapapp.views.test, name='test'),
 
    
    path('test_back/', include('cafemapapp.urls')),
]
