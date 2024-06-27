from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .filters import PostFilter
from .forms import AddPostForm, AddNewsForm, CreateCommentForm
from .models import Post, News, Category, Comment
from .utils import DataMixin


class IndexPageView(DataMixin, ListView):
    '''главная страница с новостями платформы'''

    model = News
    template_name = 'ads/index.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Главная страница')


class CategoryPageView(DataMixin, ListView):
    '''страница всех категорий'''

    model = Category
    template_name = 'ads/category/category_page.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Классы')


class AllPostPageView(DataMixin, ListView):
    '''страница всех объявлений от свежих к старым'''

    model = Post
    template_name = 'ads/post/all_posts_page.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context,
                                      title='Все объявления',
                                      filterset=self.filterset)


class PostDetailPageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DetailView):
    '''страница конкретного поста'''

    model = Post
    template_name = 'ads/post/post_detail_page.html'
    slug_url_kwarg = 'post_slug'
    slug_field = 'post_slug'
    context_object_name = 'post'
    permission_required = ['ads.view_post', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)


class PostCreatePageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    '''добавление поста'''

    form_class = AddPostForm
    template_name = 'ads/post/add_post.html'
    permission_required = ['ads.create_post', ]

    def form_valid(self, form):
        '''автоматическое присвоения автора'''

        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Добавить объявление')


class PostUpdatePageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, UpdateView):
    '''редактирование объявления'''

    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'ads/post/add_post.html'
    slug_field = 'post_slug'
    slug_url_kwarg = 'post_slug'
    permission_required = ['ads.change_post', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Редактировать объявление')


class UserPostPageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, ListView):
    '''страница объявлений пользователя'''

    model = Post
    template_name = 'ads/post/user_post_page.html'
    context_object_name = 'posts'
    permission_required = ['ads.change_post', ]
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Мои объявления')


class PostFromCategoryPageView(PermissionRequiredMixin, DataMixin, ListView):
    '''страница объявлений по категориям'''

    model = Post
    template_name = 'ads/post/post_from_category_page.html'
    context_object_name = 'posts'
    permission_required = ['ads.view_post', ]
    paginate_by = 3

    def get_queryset(self):
        self.category = Category.objects.get(category_slug=self.kwargs['category_slug'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f"Объявления по классу: {self.category}")


def close_post(request, post_slug):
    '''закрыть объявление, поле closed  в модели Post переводит в True'''

    post = Post.objects.get(post_slug=post_slug)
    post.closed = True
    post.save()
    return redirect('ads:post_detail', post_slug=post_slug)


class NewsDetailPageView(PermissionRequiredMixin, DataMixin, DetailView):
    '''страница конкретного поста'''

    model = News
    template_name = 'ads/news/news_detail_page.html'
    slug_url_kwarg = 'news_slug'
    slug_field = 'news_slug'
    context_object_name = 'news'
    permission_required = ['ads.view_news', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['news'].title)


class NewsCreatePageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    '''добавление новости'''

    model = News
    form_class = AddNewsForm
    template_name = 'ads/news/add_news.html'
    permission_required = ['ads.create_news', ]

    def form_valid(self, form):
        '''автоматическое присвоение автора'''

        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Добавить новость')


class CommentCreatePageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    '''создание комментария к посту'''

    model = Comment
    form_class = CreateCommentForm
    template_name = 'ads/comment/add_comment.html'
    context_object_name = 'comment'
    permission_required = ['ads.create_comment', ]

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


class UserIncomingCommentsPageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, ListView):
    '''страница входящих откликов'''

    model = Comment
    template_name = 'ads/comment/user_incoming_comment_page.html'
    context_object_name = 'comment'
    permission_required = ['ads.view_comment', ]
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Входящие отклики')

    def get_queryset(self):
        return Comment.objects.filter(destination_user=self.request.user)


class UserOutgoingCommentsPageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, ListView):
    '''страница исходящих откликов'''

    model = Comment
    template_name = 'ads/comment/user_outgoing_comment_page.html'
    context_object_name = 'comment'
    permission_required = ['ads.view_comment', ]
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Исходящие отклики')

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user).exclude(destination_user=self.request.user)


class CommentDetailPageView(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, DetailView):
    '''страница конкретного отклика'''

    model = Comment
    template_name = 'ads/comment/comment_detail_page.html'
    context_object_name = 'comment'
    permission_required = ['ads.view_comment', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context,
                                      title=f"От {context['comment'].author} | Получен: {context['comment'].time_create}")


def comment_receive(request, pk):
    '''если получатель принимает отклик, то в модели Comment поле received становится True. Изначально оно всегда False(не принят)
     Устанавливает параметр processed в True'''

    comment = Comment.objects.get(id=pk)
    comment.received = True
    comment.rejected = False
    comment.processed = True
    comment.save()
    return redirect('ads:comment_detail', pk=pk)


def comment_rejected(request, pk):
    '''срабатывает, когда отклик отклонили. Устанавливает параметр processed в True'''

    comment = Comment.objects.get(id=pk)
    comment.received = False
    comment.rejected = True
    comment.processed = True
    comment.save()
    return redirect('ads:comment_detail', pk=pk)
