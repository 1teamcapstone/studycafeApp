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

    like = request.POST.get('like_button') # keyword를 입력받음
    #sca_name=Studycafes.objects.filter(id=like).only("name")
    #sca_like=Studycafes.objects.filter(id=like).only("sca_like")

    if like:        
        item=Studycafes.objects.get(pk=like)
        if item.sca_like==0:
        # print(Studycafes.pk)
        # print(like)
        # print(sca_name)
            item.sca_like=1
            item.save()
        else:
            item.sca_like=0
            item.save()
    return render(request,'scainfoapp/all.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})

def sca_detail(request, pk):
    hashtags=Hashtags.objects.all()
    studycafe=get_object_or_404(Studycafes, id=pk)
    # sca_list=Studycafes.objects.order_by('-star_rating')
    # paginator=Paginator(sca_list,5)
    # page=request.GET.get('page')
    # posts=paginator.get_page(page)
    like = request.POST.get('like_button') # keyword를 입력받음
    #sca_name=Studycafes.objects.filter(id=like).only("name")
    #sca_like=Studycafes.objects.filter(id=like).only("sca_like")

    if like:        
        #item=Studycafes.objects.get(pk=like)
        if studycafe.sca_like==0:
        # print(Studycafes.pk)
        # print(like)
        # print(sca_name)
            studycafe.sca_like=1
            studycafe.save()
        else:
            studycafe.sca_like=0
            studycafe.save()
    return render(request,'scainfoapp/sca_detail.html',{'studycafe':studycafe, 'hashtags':hashtags})


def sortstar_view(request):
    hashtags=Hashtags.objects.all()
    studycafes=Studycafes.objects
    sca_list=Studycafes.objects.order_by('-star_rating')
    paginator=Paginator(sca_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    like = request.POST.get('like_button') # keyword를 입력받음
    #sca_name=Studycafes.objects.filter(id=like).only("name")
    #sca_like=Studycafes.objects.filter(id=like).only("sca_like")

    if like:        
        item=Studycafes.objects.get(pk=like)
        if item.sca_like==0:
        # print(Studycafes.pk)
        # print(like)
        # print(sca_name)
            item.sca_like=1
            item.save()
        else:
            item.sca_like=0
            item.save()
    return render(request,'scainfoapp/sort_star.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})

def sortreview_view(request):
    hashtags=Hashtags.objects.all()
    studycafes=Studycafes.objects
    sca_list=Studycafes.objects.order_by('-review')
    paginator=Paginator(sca_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    like = request.POST.get('like_button') # keyword를 입력받음
    #sca_name=Studycafes.objects.filter(id=like).only("name")
    #sca_like=Studycafes.objects.filter(id=like).only("sca_like")

    if like:        
        item=Studycafes.objects.get(pk=like)
        if item.sca_like==0:
        # print(Studycafes.pk)
        # print(like)
        # print(sca_name)
            item.sca_like=1
            item.save()
        else:
            item.sca_like=0
            item.save()
    return render(request,'scainfoapp/sort_review.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})

def like_view(request):
    hashtags=Hashtags.objects.all()
    studycafes=Studycafes.objects
    like_list=Studycafes.objects.filter(sca_like=1).all()
    paginator=Paginator(like_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    like = request.POST.get('like_button') # keyword를 입력받음
    #sca_name=Studycafes.objects.filter(id=like).only("name")
    #sca_like=Studycafes.objects.filter(id=like).only("sca_like")

    if like:        
        item=Studycafes.objects.get(pk=like)
        if item.sca_like==0:
        # print(Studycafes.pk)
        # print(like)
        # print(sca_name)
            item.sca_like=1
            item.save()
        else:
            item.sca_like=0
            item.save()
    return render(request,'scainfoapp/like.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})


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
        
        elif keyword:
            hashtags=Hashtags.objects.all()

            studycafes= Studycafes.objects.filter(name = keyword) # 해당 상호명을 가진 studycafe 저장

            return render(request, 'scainfoapp/search_result.html', {'studycafes':studycafes, 'keyword':keyword, 'hashtags':hashtags})

        else: 
            return redirect('/scainfo/all/')
        
        # like = request.POST.get('like_button') # keyword를 입력받음

        # if like:        
        #     item=Studycafes.objects.get(pk=like)
        #     if item.sca_like==0:
        #     # print(Studycafes.pk)
        #     # print(like)
        #     # print(sca_name)
        #         item.sca_like=1
        #         item.save()
        #     else:
        #         item.sca_like=0
        #         item.save()
        #     return render(request,'scainfoapp/search_result.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})
            

def searchsort_view(request, kw):
    hashtags=Hashtags.objects.all()
    keyword = request.POST.get('search_button') # keyword를 입력받음
    kw=keyword.split('#')
    scaid=Hashtags.objects.filter(name=kw[1]).values_list('sca_id')

    studycafes= Studycafes.objects.filter(id__in = scaid) # 해당 태그를 가진 studycafe 저장

    print(keyword)

    studycafes=Studycafes.objects.filter(name = keyword).order_by('-star_rating')
    sca_list=Studycafes.objects

    return render(request, 'scainfoapp/result_sort_star.html', {'studycafes':studycafes, 'keyword':keyword, 'hashtags':hashtags})
        
