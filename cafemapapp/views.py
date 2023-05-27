from rest_framework.response import Response    #추가
from rest_framework.decorators import api_view  #추가
from django.shortcuts import render,get_object_or_404,redirect
from .models import Studycafes  #추가
from .serializers import TestDataSerializer #추가
from django.core.paginator import Paginator
from .models import Hashtags
from userlocation.models import UserLocation


@api_view(['GET'])
def getTestDatas(request):
   datas = Hashtags.objects.all()
   serializer = TestDataSerializer(datas, many=True)
   return Response(serializer.data)

# def test_view(request):
#     blogs=Studycafes.objects
#     blog_list=Studycafes.objects.all()
#     paginator=Paginator(blog_list,5)
#     page=request.GET.get('page')
#     posts=paginator.get_page(page)
#     return render(request,'cafemapapp/home.html',{'blogs':blogs, 'posts':posts})

# def post_view(request):
#     studycafe=Studycafes.objects.all()
#     #print(studycafe)
#     return render(request, 'cafemapapp/scadatatest.html',{'studycafe':studycafe})

def studycafe_view(request):
    studycafe=Studycafes.objects.all()
    location=UserLocation.objects.first()
    #location=UserLocation.objects.last()
    #print(studycafe)
    #print(location)
    return render(request, 'cafemapapp/scamap.html',{'studycafe':studycafe, 'location':location})

def maptest_view(request, pk):
    studycafe=get_object_or_404(Studycafes, id=pk)
    #print(studycafe)
    return render(request, 'cafemapapp/onemarker.html',{'studycafe':studycafe})


# Create your views here.
# def index(request):
#     return render(request, 'cafemapapp/index.html')

# def map(request):
#     return render(request, 'cafemapapp/studycafeMap.html')

def study(request):
    return render(request, 'cafemapapp/studytest.html')

def map(request):
    return render(request, 'cafemapapp/test2.html')

# def sca(request):
#     return render(request, 'cafemapapp/scadatatest.html')