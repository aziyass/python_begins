from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('articles/', views.show_all_articles, name='articles'),
    path('article/<int:article_id>/', views.show_article, name='article'),
    path('about/', views.about, name='about'),
]