from django.test import TestCase
from django.urls import resolve

from articles.views import main_page


class MainPageTest(TestCase):
    """Проверка главной страницы"""

    def test_correct_url_resolves_to_main_page_view(self):
        self.assertEqual(resolve('/').func, main_page)
