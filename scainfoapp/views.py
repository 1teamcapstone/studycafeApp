from django.shortcuts import render,get_object_or_404,redirect
from cafemapapp.models import Studycafes
from django.core.paginator import Paginator
from cafemapapp.models import Hashtags

# Create your views here.
def test_view(request):
    hashtags=Hashtags.objects.all()
    studycafes=Studycafes.objects
    sca_list=Studycafes.objects.all()
    paginator=Paginator(sca_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'scainfoapp/all.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})

def sortstar_view(request):
    hashtags=Hashtags.objects.all()
    studycafes=Studycafes.objects
    sca_list=Studycafes.objects.order_by('-star_rating')
    paginator=Paginator(sca_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'scainfoapp/sort_star.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})

def sortreview_view(request):
    hashtags=Hashtags.objects.all()
    studycafes=Studycafes.objects
    sca_list=Studycafes.objects.order_by('-review')
    paginator=Paginator(sca_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'scainfoapp/sort_review.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})


#hash tag 검색
def hashtag_view(request):    
        hashtags=Hashtags.objects.all()       
        keyword = request.POST.get('search_button') # keyword를 입력받음
        print(keyword)
        if '#' in keyword:
            kw=keyword.split('#')
            scaid=Hashtags.objects.filter(name=kw[1]).values_list('sca_id')

            studycafes= Studycafes.objects.filter(id__in = scaid) # 해당 태그를 가진 studycafe 저장

            return render(request, 'scainfoapp/search_result.html', {'studycafes':studycafes, 'keyword':keyword, 'hashtags':hashtags})

        else: 
            hashtags=Hashtags.objects.all()
            studycafes=Studycafes.objects
            sca_list=Studycafes.objects.all()
            paginator=Paginator(sca_list,5)
            page=request.GET.get('page')
            posts=paginator.get_page(page)
            return render(request,'scainfoapp/all.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})
