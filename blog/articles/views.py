from django.shortcuts import render

from articles.models import Article, Tag


def main_page(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'articles/main_page.html', context=context)
