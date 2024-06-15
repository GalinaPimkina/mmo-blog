from django.urls import path

from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('categories/', views.CategoryView.as_view(), name='categories'),

    path('posts/', views.PostView.as_view(), name='all_posts'),
    path('posts/add/', views.PostCreateView.as_view(), name='add_post'),
    path('posts/<str:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
]