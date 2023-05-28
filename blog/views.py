from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cafemapapp.models import Studycafes

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 추가한 부분
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)

    try:
        paginated_list = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        paginated_list = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        paginated_list = paginator.get_page(page)
    
    return render(request, 'blog/post_list.html', {'posts': posts, 'paginated_list': paginated_list, 'paginator': paginator})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def study_view(request,pk):        
    studycafe=get_object_or_404(Studycafes, id=pk)
    #print(studycafe.name)
    study=Post.objects.filter(study_place=studycafe.name).all()
    #print(study)

    return render(request,'blog/study_view.html',{'studycafe':studycafe, 'study':study})
