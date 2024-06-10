from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post, News, Category
from .utils import DataMixin


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


class PostDetailView(DataMixin, DetailView):
    '''страница конкретного поста'''

    model = Post
    template_name = 'ads/post_detail_page.html'
    slug_url_kwarg = 'post_slug'
    slug_field = 'post_slug'
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     context =super().get_context_data(**kwargs)
    #     return self.get_mixin_context(context,
    #                             title=context['post'].title,
    #             )
