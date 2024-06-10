from django.shortcuts import render
from django.views.generic import ListView

from .models import Post, News, Category


class IndexView(ListView):
    '''главная страница с новостями'''
    model = News
    template_name = 'ads/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Home page',
    }

class CategoryView(ListView):
    '''страница всех категорий'''

    model = Category
    template_name = 'ads/category_page.html'
    context_object_name = 'categories'
    extra_context = {
        'title': 'Categories',
    }


class PostView(ListView):
    '''страница всех объявлений от свежих к старым'''

    model = Post
    template_name = 'ads/all_posts_page.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'All ads',
    }