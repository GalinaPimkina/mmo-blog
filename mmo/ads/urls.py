from django.urls import path

from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'), #главная страница

    path('news/add/', views.NewsCreatePageView.as_view(), name='add_news'), #добавить новость
    path('news/<str:news_slug>/', views.NewsDetailPageView.as_view(), name='news_detail'),#страница выбранной новости

    path('categories/', views.CategoryPageView.as_view(), name='categories'),#страница категорий

    path('posts/', views.AllPostPageView.as_view(), name='all_posts'),#страница со всеми объявлениями о поиске
    path('posts/category/<str:category_slug>/', views.PostFromCategoryPageView.as_view(), name='post_from_category'), #страница объявлений по категориям
    path('posts/user/', views.UserPostPageView.as_view(), name='user_post_page'),#страница объявлений конкретного юзера

    path('post/add/', views.PostCreatePageView.as_view(), name='add_post'),#добавить объявление
    path('post/<str:post_slug>/', views.PostDetailPageView.as_view(), name='post_detail'),#страница выбранного объявления
    path('post/<str:post_slug>/edit/', views.PostUpdatePageView.as_view(), name='edit_post'),#редактирование объявления
    path('post/<str:post_slug>/close/', views.close_post, name='close_post'),# закрыть объявление
    path('post/<str:post_slug>/add_comment/', views.CommentCreatePageView.as_view(), name='add_comment'),#добавить комментарий

    path('comment/<int:pk>/', views.CommentDetailPageView.as_view(), name='comment_detail'),#страница выбранного комментария
    path('comments/incoming/', views.UserIncomingCommentsPageView.as_view(), name='comments_incoming'),#страница с входящими откликами пользователя
    path('comments/outgoing/', views.UserOutgoingCommentsPageView.as_view(), name='comments_outgoing'),#страница с исходящими откликами пользователя

    path('comment/<int:pk>/receive/', views.comment_receive, name='comment_receive'), #если отклик принят
    path('comment/<int:pk>/rejected/', views.comment_rejected, name='comment_rejected'),#если отклик отклонен
]