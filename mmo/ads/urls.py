from django.urls import path

from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),

    path('news/add/', views.NewsCreatePageView.as_view(), name='add_news'),
    path('news/<str:news_slug>/', views.NewsDetailPageView.as_view(), name='news_detail'),

    path('categories/', views.CategoryPageView.as_view(), name='categories'),

    path('posts/', views.AllPostPageView.as_view(), name='all_posts'),
    path('post/add/', views.PostCreatePageView.as_view(), name='add_post'),
    path('post/<str:post_slug>/', views.PostDetailPageView.as_view(), name='post_detail'),

    path('post/<str:post_slug>/add_comment/', views.CommentCreatePageView.as_view(), name='add_comment'),
]