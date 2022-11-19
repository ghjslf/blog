from django.test import TestCase
from django.urls import resolve

from articles.views import home_page


class HomePageTest(TestCase):
    """Проверка домашней страницы"""

    def test_correct_url_resolves_to_home_page_view(self):
        self.assertEqual(resolve('/').func, home_page)
