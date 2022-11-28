from django.shortcuts import render

from articles.models import Article, Tag


def main_page(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'articles/main_page.html', context=context)

def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        "article": article,
    }
    return render(request, 'articles/article_page.html', context=context)
