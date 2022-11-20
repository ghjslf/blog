from django.urls import resolve 
from django.test import TestCase 
from django.http import HttpRequest

from articles.views import main_page


class MainPageTest(TestCase):
    """Проверка главной страницы"""

    def test_correct_url_resolves_to_main_page_view(self):
        self.assertEqual(resolve('/').func, main_page)

    def test_main_page_view_content_contains_correct_html(self):
        """Проверяем, что view главной страницы возвращает текст обернутый в <html></html>"""
        request = HttpRequest()
        response = main_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue(html.endswith('</html>'))

    def test_main_page_view_content_contains_correct_title(self):
        request = HttpRequest()
        response = main_page(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Блог Никиты Пашкова</title>', html)