from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Album, News
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class HomeView(ListView):
    model = Album, News
    template_name = 'coder/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


def index(request):
    all_albums = Album.objects.all()
    news_results = News.objects.all()

    query = request.GET.get("q")
    if query:
        all_albums = all_albums.filter(Q(album_title__icontains=query) | Q(genre__icontains=query)).distinct()

    return render(request, 'coder/index.html', {'all_albums': all_albums, 'news': news_results})


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'coder/detail.html', {'album': album})


def story(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'coder/story.html', {'news': news})


def about(request):
    return render(request, 'coder/about.html')


def contact(request):
    return render(request, 'coder/contact.html')


def team(request):
    return render(request, 'coder/team.html')
