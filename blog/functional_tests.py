from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class MainPageTest(unittest.TestCase):
    """Проверка отображения элементов главной страницы"""

    def setUp(self):
        """Открытие страницы блога в браузере"""
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000")

    def tearDown(self):
        """Закрытие окна браузера"""
        self.browser.quit()

    def test_title_display(self):
        """Проверка отображения заголовка сайта во вкладке браузера"""
        self.assertEqual("Блог Никиты Пашкова", self.browser.title)

    def test_header_display(self):
        """Проверка отображения заголовка сайта на странице"""
        header = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Блог Никиты Пашкова", header, "No header")

    def test_articles_list_display(self):
        """Проверка отображения списка статей"""   
        articles_list = self.browser.find_element(By.CLASS_NAME, "articles_list")
        self.assertIsNotNone(articles_list, "No articles list")


if __name__ == "__main__":
    unittest.main()