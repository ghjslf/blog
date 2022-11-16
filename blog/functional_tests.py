from selenium import webdriver
import unittest


class MainPageTest(unittest.TestCase):
    """Проверка отображения элементов главной страницы"""

    def setUp(self):
        """Открытие страницы блога в браузере"""

        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000")


    def tearDown(self):
        """Закрытие окна браузера"""

        self.browser.close()


    def test_title_display(self):
        """Проверка отображения заголовка сайта во вкладке браузера"""
        
        self.assertEqual("ghjslf", self.browser.title)


if __name__ == "__main__":
    unittest.main()