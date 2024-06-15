from django.views.generic import ListView, DetailView

from .models import Post, News, Category
from .utils import DataMixin


class IndexView(DataMixin, ListView):
    '''главная страница с новостями'''
    model = News
    template_name = 'ads/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Главная страница')


class CategoryView(DataMixin, ListView):
    '''страница всех категорий'''

    model = Category
    template_name = 'ads/category_page.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Классы')


class PostView(DataMixin, ListView):
    '''страница всех объявлений от свежих к старым'''

    model = Post
    template_name = 'ads/all_posts_page.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Все объявления')


class PostDetailView(DataMixin, DetailView):
    '''страница конкретного поста'''

    model = Post
    template_name = 'ads/post_detail_page.html'
    slug_url_kwarg = 'post_slug'
    slug_field = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)


