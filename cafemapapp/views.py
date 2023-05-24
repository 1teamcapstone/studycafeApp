from rest_framework.response import Response    #추가
from rest_framework.decorators import api_view  #추가
from django.shortcuts import render,get_object_or_404,redirect
from .models import Studycafes  #추가
from .serializers import TestDataSerializer #추가
from django.core.paginator import Paginator


@api_view(['GET'])
def getTestDatas(request):
    datas = Studycafes.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

def test_view(request):
    blogs=Studycafes.objects
    blog_list=Studycafes.objects.all()
    paginator=Paginator(blog_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'cafemapapp/home.html',{'blogs':blogs, 'posts':posts})


def post_view(request):
    studycafe=Studycafes.objects.all()
    #print(studycafe)
    return render(request, 'cafemapapp/scadatatest.html',{'studycafe':studycafe})

def studycafe_view(request):
    studycafe=Studycafes.objects.all()
    #print(studycafe)
    return render(request, 'cafemapapp/test3.html',{'studycafe':studycafe})

# Create your views here.
def index(request):
    return render(request, 'cafemapapp/index.html')

def map(request):
    return render(request, 'cafemapapp/studycafeMap.html')

def study(request):
    return render(request, 'cafemapapp/studytest.html')

def test(request):
    return render(request, 'cafemapapp/test3.html')

# def sca(request):
#     return render(request, 'cafemapapp/scadatatest.html')