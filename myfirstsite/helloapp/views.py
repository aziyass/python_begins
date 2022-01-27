from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home(request):
    return render(request, "home.html")
    
def about(request):
    return render(request, "about.html")

def show_article(request, article_id):
    context = {
        'article': Article.objects.get(id=article_id)
    }
    return render(request, "article.html", context)

def show_all_articles(request):
    context = {
        'all_articles_list': Article.objects.all()
    }
    return render(request, "articles.html", context)