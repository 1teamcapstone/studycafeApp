from django.shortcuts import render,get_object_or_404,redirect
from cafemapapp.models import Studycafes
from django.core.paginator import Paginator
from cafemapapp.models import Hashtags

# Create your views here.
def test_view(request):
    hashtags=Hashtags.objects.all()
    blogs=Studycafes.objects
    blog_list=Studycafes.objects.all()
    paginator=Paginator(blog_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'scainfoapp/all.html',{'blogs':blogs, 'posts':posts, 'hashtags':hashtags})


#hash tag 검색
def hashtag_view(request):
    
        hashtags=Hashtags.objects.all()
        #blogs=Studycafes.objects
        #blog_list=Studycafes.objects.all()        
        keyword = request.POST.get('search_button') # keyword를 입력받음
        print(keyword)
        if '#' in keyword:
            kw=keyword.split('#')
            print(kw)
        #tag = Hashtags.objects.filter(name=keyword) # 해당 키워드를 가진 tag 클래스 오픈
            scaid=Hashtags.objects.filter(name=kw[1]).values_list('sca_id')

            studycafes= Studycafes.objects.filter(id__in = scaid) # 해당 태그를 가진 studycafe 저장
            # sca_list=Studycafes.objects.filter(id__in = scaid).all()
            # paginator=Paginator(sca_list,5)
            # page=request.GET.get('page')
            # posts=paginator.get_page(page)
        #print(scaid)
        #print(studycafes)
            return render(request, 'scainfoapp/search_result.html', {'studycafes':studycafes, 'keyword':keyword, 'hashtags':hashtags})

        else: 
            hashtags=Hashtags.objects.all()
            blogs=Studycafes.objects
            blog_list=Studycafes.objects.all()
            paginator=Paginator(blog_list,5)
            page=request.GET.get('page')
            posts=paginator.get_page(page)
            return render(request,'scainfoapp/all.html',{'blogs':blogs, 'posts':posts, 'hashtags':hashtags})

        
    # elif request.method == 'GET':
    #     return redirect('/')