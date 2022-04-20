from locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

class MainPage(BasePage):
    def click_to_attractions_tab(self):
        element = self.driver.find_element(*MainPageLocators.ATTRACTIONS_TAB)
        element.click()

    def send_text_to_search_input(self, text):
        element = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        element.send_keys(text)

    def click_to_search(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH
            ,MainPageLocators.CHECK_ELEMENT_AT_LIST)))
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()

class SearchPage(BasePage):
    def check_the_checkebox(self,checnbox_name):
        if (checnbox_name == "museums"):
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH
                ,MainPageLocators.MUSEUM_CHECKBOX)))
        else:
            pass
        element.click()

    def click_to_first_news(self):
        element = self.driver.find_element(*MainPageLocators.FIRST_ELEMENT)
        element.click()
    
    def first_news_title(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH
            ,MainPageLocators.FIRST_ELEMENT_TEXT))).text
    
    def change_window_handle(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def title_name(self):
        return self.driver.title
