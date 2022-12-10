from django.http.request import HttpRequest
from django.http import Http404
from django.shortcuts import render

from articles.models import Article, Tag


def main_page(request: HttpRequest):
    query = request.GET.get('q')
    tags = request.GET.getlist('tag')

    if not tags:
        if not query:
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(content__icontains=query)
    else:
        if not query:
           articles = Article.objects.filter(tags__title__in=tags).distinct()
        else:
            articles = Article.objects.filter(tags__title__in=tags, content__icontains=query).distinct()
        
    
    context = {
        "articles": articles,
    }
    return render(request, 'articles/main_page.html', context=context)

def article_page(request: HttpRequest, article_id: int):
    try:
        article = Article.objects.get(pk=article_id)
    except:
        raise Http404

    context = {
        "article": article,
    }
    return render(request, 'articles/article_page.html', context=context)
