from rest_framework.response import Response    #추가
from rest_framework.decorators import api_view  #추가
from django.shortcuts import render
from .models import Studycafes  #추가
from .serializers import TestDataSerializer #추가

@api_view(['GET'])
def getTestDatas(request):
    datas = Studycafes.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)


# Create your views here.
def index(request):
    return render(request, 'cafemapapp/index.html')

def map(request):
    return render(request, 'cafemapapp/studycafeMap.html')

def study(request):
    return render(request, 'cafemapapp/studytest.html')

def test(request):
    return render(request, 'cafemapapp/test2.html')