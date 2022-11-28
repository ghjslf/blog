from django.urls import resolve 
from django.test import TestCase 
from django.http import HttpRequest

from articles.views import main_page
from articles.models import Article, Tag


class MainPageTest(TestCase):
    """Проверка главной страницы"""

    def test_correct_url_resolves_to_main_page_view(self):
        self.assertEqual(resolve('/').func, main_page)

    def test_main_page_view_content_contains_correct_html(self):
        """Проверяем, что view главной страницы возвращает текст обернутый в <html></html>"""
        request = HttpRequest()
        response = main_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertTrue(html.strip().endswith('</html>'))

    def test_main_page_view_content_contains_correct_title(self):
        request = HttpRequest()
        response = main_page(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Блог Никиты Пашкова</title>', html)

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

        # self.assertIn(test_article.title, html)
        # for tag in test_article.tags.all():
        #     self.assertIn(tag.title, html)
        # self.assertNotIn(test_article.content, html)
        
        # self.assertIn(another_test_article.title, html)
        # for tag in another_test_article.tags.all():
        #     self.assertIn(tag.title, html)
        # self.assertNotIn(another_test_article.content, html)
        
        
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
        response = article_page(request)
        html = response.content.decode('utf-8')

        self.assertIn("Title 1", html)
        self.assertNotIn("Annotation 1", html)
        self.assertIn("test", html)
        self.assertIn("Content 1", html)