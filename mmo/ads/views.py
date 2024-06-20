from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm, AddNewsForm, CreateCommentForm
from .models import Post, News, Category, Comment
from .utils import DataMixin


class IndexPageView(DataMixin, ListView):
    '''главная страница с новостями'''
    model = News
    template_name = 'ads/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Главная страница')


class CategoryPageView(DataMixin, ListView):
    '''страница всех категорий'''

    model = Category
    template_name = 'ads/category_page.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Классы')


class AllPostPageView(DataMixin, ListView):
    '''страница всех объявлений от свежих к старым'''

    model = Post
    template_name = 'ads/all_posts_page.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Все объявления')


class PostDetailPageView(DataMixin, DetailView):
    '''страница конкретного поста'''

    model = Post
    template_name = 'ads/post_detail_page.html'
    slug_url_kwarg = 'post_slug'
    slug_field = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)


class PostCreatePageView(LoginRequiredMixin, DataMixin, CreateView):
    '''добавление поста'''

    form_class = AddPostForm
    template_name = 'ads/add_post.html'

    def form_valid(self, form):
        '''автоматическое присвоения автора'''

        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Добавить объявление')


class NewsDetailPageView(DataMixin, DetailView):
    '''страница конкретного поста'''

    model = News
    template_name = 'ads/news_detail_page.html'
    slug_url_kwarg = 'news_slug'
    slug_field = 'news_slug'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['news'].title)


class NewsCreatePageView(LoginRequiredMixin, DataMixin, CreateView):
    '''добавление новости'''

    model = News
    form_class = AddNewsForm
    template_name = 'ads/add_news.html'

    def form_valid(self, form):
        '''автоматическое присвоение автора'''

        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Добавить новость')


class CommentCreatePageView(LoginRequiredMixin, DataMixin, CreateView):
    model = Comment
    form_class = CreateCommentForm
    template_name = 'ads/add_comment.html'
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Отправить отклик',)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = Post.objects.get(post_slug=self.kwargs['post_slug'])
        comment.destination_user = comment.post.author
        comment.save()
        return redirect('ads:index')

