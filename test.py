import unittest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
import page

class PythonTest(unittest.TestCase):
    """Class PythonTest"""
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chromedriver_autoinstaller.install(cwd=True)
            ,options=self.options)
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.get("https://www.booking.com/index.en-gb.html")

    def test_find(self):
        """test 1"""
        main_page = page.MainPage(self.driver, self.wait)
        search_page = page.SearchPage(self.driver, self.wait)

        main_page.click_to_attractions_tab()
        main_page.send_text_to_search_input("travel")
        main_page.click_to_search()
        search_page.check_the_checkebox("museums")
        news_title = search_page.first_news_title()
        search_page.click_to_first_news()
        search_page.change_window_handle()

        self.assertTrue(news_title in self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
