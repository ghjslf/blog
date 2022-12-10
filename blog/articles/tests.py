from django.urls import resolve 
from django.test import TestCase 
from django.http import HttpRequest

from articles.views import main_page, article_page
from articles.models import Article, Tag


class MainPageTest(TestCase):
    """Проверка главной страницы"""

    def test_articles_list_display(self):
        """Проверяем, что на главной странице отображаются статьи из базы данных"""
        test_tag = Tag(
            title="test"
        )
        test_tag.save()

        test_article = Article(
            title="Title 1",
            annotation="Annotation 1",
            content="Content 1"
        )
        test_article.save()
        test_article.tags.add(test_tag)

        another_test_article = Article(
            title="Title 2",
            annotation="Annotation 2",
            content="Content 2"
        )
        another_test_article.save()
        another_test_article.tags.add(test_tag)

        request = HttpRequest()
        response = main_page(request)
        html = response.content.decode('utf-8')

        self.assertIn("Title 1", html)
        self.assertIn("/1", html)
        self.assertIn("test", html)
        self.assertNotIn("Content 1", html)
        
        self.assertIn("Title 2", html)
        self.assertIn("/2", html)
        self.assertIn("test", html)
        self.assertNotIn("Content 2", html)
        
        
class ArticlePageTest(TestCase):
    """Проверка страницы конкретной статьи"""

    def test_article_display(self):
        """Проверяем, что на странице статьи отображаются все ее нужные поля"""
        test_tag = Tag(
            title="test"
        )
        test_tag.save()

        test_article = Article(
            title="Title 1",
            annotation="Annotation 1",
            content="Content 1"
        )
        test_article.save()
        test_article.tags.add(test_tag)

        request = HttpRequest()
        response = article_page(request, 1)
        html = response.content.decode('utf-8')

        self.assertIn("Title 1", html)
        self.assertNotIn("Annotation 1", html)
        self.assertIn("test", html)
        self.assertIn("Content 1", html)