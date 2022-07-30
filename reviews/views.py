from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Review
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    review = Review.objects.all()
    paginator = Paginator(review, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'reviews/index.html', {'page':page})

def search(request):
    if request.method=="POST":
        searched = request.POST['searched']
        anime = Review.objects.filter(title__contains=searched)
        return render(request, 'reviews/searchresultsrework.html', {'searched':searched, 'reviews':anime})
    else:
        return render(request, 'reviews/searchresultsrework.html', {})


def rate(request, anime_pk):
    anime = get_object_or_404(Review, pk=anime_pk)
    if request.method=='POST':
        score = request.POST['score']
        anime.totalscore += int(score)
        anime.votes+=1
        anime.userscore = anime.totalscore//anime.votes
        anime.save()
        return render(request, 'reviews/result.html', {'anime':anime})
        # return redirect('result')
    else:
        return render(request, 'reviews/rate.html', {'anime':anime})

def result(request, anime_pk):
    anime = get_object_or_404(Review, pk=anime_pk)
    return render(request, 'reviews/result.html', {'anime':anime})
