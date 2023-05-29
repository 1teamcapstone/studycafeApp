from django.shortcuts import render,get_object_or_404,redirect
from cafemapapp.models import Studycafes
from django.core.paginator import Paginator
from cafemapapp.models import Hashtags
from cafemapapp.models import Search
from cafemapapp.models import Sort
from userlocation.models import UserLocation

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
        item_l=Studycafes.objects.get(pk=like)
        if item_l.sca_like==0:
        # print(Studycafes.pk)
        # print(like)
        # print(sca_name)
            item_l.sca_like=1
            item_l.save()
        else:
            item_l.sca_like=0
            item_l.save()
    return render(request,'scainfoapp/like.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})


#hash tag 검색
def hashtag_view(request):    
        hashtags=Hashtags.objects.all()       
        kw = request.POST.get('search_button') # keyword를 입력받음
        st = request.POST.get('sort_button')
        print(kw)
        print(st,"변수")       
        sort=Sort.objects.get(pk=1)
        print(sort.sort,"db")
        like = request.POST.get('like_button') # keyword를 입력받음
        map = request.POST.get('map_button')          
        if like:        
            item_l=Studycafes.objects.get(pk=like)
            if item_l.sca_like==0:
                    # print(Studycafes.pk)
                print(like,'찜하기 되나?')
                    # print(sca_name)
                item_l.sca_like=1
                item_l.save()
                return redirect('/scainfo/like/') 
            else:
                item_l.sca_like=0
                item_l.save()
        
        if map:
            item=Search.objects.get(pk=1)
            kwd=item.keyword.split('#')
            print(kwd,"첫번재 if")
            kwd2=kwd[1]
            scaid=Hashtags.objects.filter(name=kwd2).values_list('sca_id')
            studycafe= Studycafes.objects.filter(id__in = scaid) # 해당 태그를 가진 studycafe 저장
            location=UserLocation.objects.last()
            return render(request, 'cafemapapp/searchmap.html',{'studycafe':studycafe, 'location':location})
        
        if kw is not None and st is None:
            item=Search.objects.get(pk=1)
            item.keyword=kw
            # print(item.keyword)
            # print(kw)
            item.save()
            if '#' in item.keyword:
                kwd=item.keyword.split('#')
                print(kwd,"첫번재 if")
                kwd2=kwd[1]
                scaid=Hashtags.objects.filter(name=kwd2).values_list('sca_id')
                studycafes= Studycafes.objects.filter(id__in = scaid) # 해당 태그를 가진 studycafe 저장
                paginator=Paginator(studycafes,5)
                page=request.GET.get('page')
                posts=paginator.get_page(page)
                
            else:
                kwd2=item.keyword
                print(kwd2,"그냥 스카 이름 검색")
                scaid=Hashtags.objects.filter(name=kwd2).values_list('sca_id')
                studycafes= Studycafes.objects.filter(name=kwd2) # 해당 태그를 가진 studycafe 저장
                paginator=Paginator(studycafes,5)
                page=request.GET.get('page')
                posts=paginator.get_page(page)
                
        elif st is not None or sort.sort is not None and kw is None:
            print(st,"sort")

            if st:
                sort.sort=st
                sort.save()

            elif st is None:
                item=Search.objects.get(pk=1)
                # print(item.keyword)
                # print(kw)
                kwd=item.keyword.split('#')
                print("기본 페이징처리")
                scaid=Hashtags.objects.filter(name=kwd[1]).values_list('sca_id')
                studycafes= Studycafes.objects.filter(id__in = scaid) # 해당 태그를 가진 studycafe 저장
                paginator=Paginator(studycafes,5)
                page=request.GET.get('page')
                posts=paginator.get_page(page)                

            if sort.sort=='1':
                item=Search.objects.get(pk=1)
                kwd=item.keyword.split('#')
                scaid=Hashtags.objects.filter(name=kwd[1]).values_list('sca_id')
                studycafes= Studycafes.objects.filter(id__in = scaid) # 해당 태그를 가진 studycafe 저장
                paginator=Paginator(studycafes,5)
                page=request.GET.get('page')
                posts=paginator.get_page(page)
                
            elif sort.sort=='2':
                item=Search.objects.get(pk=1)
                kwd=item.keyword.split('#')
                scaid=Hashtags.objects.filter(name=kwd[1]).values_list('sca_id')
                studycafes= Studycafes.objects.filter(id__in = scaid).order_by('-star_rating') # 해당 태그를 가진 studycafe 저장
                paginator=Paginator(studycafes,5)
                page=request.GET.get('page')
                posts=paginator.get_page(page)
                return render(request,'scainfoapp/has_sort_star.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})
             
            elif sort.sort=='3':
                item=Search.objects.get(pk=1)
                kwd=item.keyword.split('#')
                scaid=Hashtags.objects.filter(name=kwd[1]).values_list('sca_id')
                studycafes= Studycafes.objects.filter(id__in = scaid).order_by('-review') # 해당 태그를 가진 studycafe 저장
                paginator=Paginator(studycafes,5)
                page=request.GET.get('page')
                posts=paginator.get_page(page)
                return render(request,'scainfoapp/has_sort_review.html',{'studycafes':studycafes, 'posts':posts, 'hashtags':hashtags})
            
            else: 
                return redirect('/scainfo/all/')

        

        return render(request, 'scainfoapp/search_result.html', {'studycafes':studycafes, 'posts':posts, 'keyword':item.keyword, 'hashtags':hashtags})
