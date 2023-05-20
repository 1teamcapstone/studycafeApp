from django.shortcuts import render, redirect
from .models import UserLocation
from django.http import HttpResponse

# Create your views here.

def location(request):
    if request.method == 'GET':
        return render(request, 'write.html')
    
    elif request.method == 'POST':
            location = request.POST.get('location')
            err_data={}
            if not(location):
                err_data['error'] = '주소를 입력해주세요.'
            else:
                user_location = UserLocation(
                      
                        location=location,            
                    )
                user_location.save()
                return redirect('/')
            return render(request, 'write.html',  err_data)
            