
import json
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from .models import Board, User, Comment
from .forms import BoardForm
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse

def board_write(request):
    if not request.session.get('user'):
        return redirect('/accounts/login')

    if request.method == "GET":
        form = BoardForm()

    elif request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk = user_id)
            new_board = Board(
                title = form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                writer = user
            )
            new_board.save()
            return redirect('/board/list')

    return render(request, 'board_write.html', {'form' :form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 6)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards':boards})
# Create your views here.
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board' : board})

def comment_create_ajax(request):
    comment= Comment()
    comment.body =request.POST.get('body')
    comment.board = get_object_or_404(Board, pk=request.POST.get('board_id'))
    comment.save()
    
    ret = {
        'body': comment.body,
    }
    return HttpResponse(json.dumps(ret), content_type="application/json")