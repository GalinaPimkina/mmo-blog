from django.shortcuts import render
from django.views.generic import ListView

from .models import Post, News, Category


class IndexView(ListView):
    model = News
    template_name = 'ads/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Home page',
    }

class CategoryView(ListView):
    model = Category
    template_name = 'ads/category_page.html'
    context_object_name = 'categories'
    extra_context = {
        'title': 'Categories',
    }

