import json
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from .models import Review, User 
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse

def review_write(request):
    if not request.session.get('user'):
        return redirect('/accounts/login')

    if request.method == "GET":
        form = ReviewForm()

    elif request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk = user_id)
            new_review= Review(
                contents = form.cleaned_data['contents'],
                writer = user
            )
            new_review.save()
            return redirect('/review/list')

    return render(request, 'review_write.html', {'form' :form})

def review_list(request):
    all_reviews = Review.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_reviews, 6)
    reviews = paginator.get_page(page)
    return render(request, 'review_list.html', {'reviews':reviews})
# Create your views here.


