from rest_framework.response import Response    #추가
from rest_framework.decorators import api_view  #추가
from django.shortcuts import render
from .models import Studycafes  #추가
from .serializers import TestDataSerializer #추가
#from django.views import generic

@api_view(['GET'])
def getTestDatas(request):
    datas = Studycafes.objects.all()
    serializer = TestDataSerializer(datas, many=True)
    return Response(serializer.data)

# class Sca_data(generic.TemplateView):
#     def get(self, request, *args, **kwargs):
#         template_name='cafemapapp/templates/cafemapapp/scadatatest.html'
#         sca_address=Studycafes.objects.all()
#         return render(request,template_name,{"sca_address": sca_address})

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