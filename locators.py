from selenium.webdriver.common.by import By

class MainPageLocators(object):
    ATTRACTIONS_TAB = (By.XPATH, "//span[contains(text(),'Attractions')]")
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    CHECK_ELEMENT_AT_LIST = "//li[@class='css-9dv5ti'][1]"
    MUSEUM_CHECKBOX = "//input[@value='museums']/parent::*"
    FIRST_ELEMENT = (By.XPATH, "//div[@class='c90eaff0bf c3294bb3d3']/div[1]//a")
    FIRST_ELEMENT_TEXT = "//div[@class='c90eaff0bf c3294bb3d3']/div[1]//a//h4"
