from django.shortcuts import render
from cafemapapp.models import Studycafes
from django.core.paginator import Paginator

# Create your views here.
def test_view(request):
    blogs=Studycafes.objects
    blog_list=Studycafes.objects.all()
    paginator=Paginator(blog_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'scainfoapp/home.html',{'blogs':blogs, 'posts':posts})
