from django.shortcuts import render
from django.views.generic import ListView

from .models import Post, News


class IndexView(ListView):
    model = News
    template_name = 'ads/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Home page',
    }


