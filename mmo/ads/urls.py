from django.urls import path

from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/', views.CategoryView.as_view(), name='categories'),
]