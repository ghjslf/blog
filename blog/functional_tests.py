from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class MainPageTest(unittest.TestCase):
    """Проверка отображения элементов главной страницы"""

    def setUp(self):
        """Открытие страницы блога в браузере"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Закрытие окна браузера"""
        self.browser.quit()

    def test_title_display(self):
        """Проверка отображения заголовка сайта во вкладке браузера"""
        self.browser.get("http://localhost:8000")
        self.assertEqual("GHJSLF", self.browser.title)

    def test_header_display(self):
        """Проверка отображения заголовка сайта на странице"""
        self.browser.get("http://localhost:8000")
        header = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("GHJSLF", header, "Wrong header")

    def test_articles_list_display(self):
        """Проверка отображения списка статей"""
        self.browser.get("http://localhost:8000") 
        articles_list = self.browser.find_element(By.CLASS_NAME, "articles-list")
        self.assertIsNotNone(articles_list, "No articles list")
        article = self.browser.find_element(By.CLASS_NAME, "article")
        self.assertIsNotNone(article, "No articles in list")
        article_title = self.browser.find_element(By.CLASS_NAME, "article__title")
        self.assertIsNotNone(article_title, "No title in article")
        article_annotate = self.browser.find_element(By.CLASS_NAME, "article__annotate")
        self.assertIsNotNone(article_annotate, "No annotate in article")
        tags = self.browser.find_element(By.CLASS_NAME, "article__tags-list")
        self.assertIsNotNone(tags, "No tags in article")
        tag = self.browser.find_element(By.CLASS_NAME, "article__tag")
        self.assertIsNotNone(tag, "Empty tags list")

    def test_article_link_leads_to_full_article(self):
        """Проверка ссылок на полные статьи в заголовках статей"""
        self.browser.get("http://localhost:8000")
        blocks = [(title.text, title.find_element(By.TAG_NAME, "a").get_attribute("href")) for title in self.browser.find_elements(By.CLASS_NAME, "article__title")]
        
        for title, link in blocks:
            self.browser.get(link)
            self.assertEqual(self.browser.find_element(By.CLASS_NAME, "article__title").text, title)

    def test_link_to_nonexistent_page(self):
        """Проверка обработаки несуществующих URLs""" 
        self.browser.get("http://localhost:8000/0/")
        self.assertIn("404", self.browser.find_element(By.TAG_NAME, "h1").text)


if __name__ == "__main__":
    unittest.main()