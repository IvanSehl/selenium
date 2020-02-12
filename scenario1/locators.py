from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GUESTS_FIELD = (By.ID, "xp__guests__toggle")
    ADD_CHILD = (By.XPATH, "//*[@id='xp__guests__inputs-container']/div/div/div[2]/div/div[2]/button[2]")
    
class SearchResultsPageLocators(object):
    FIELDS_CHILD_INPUT = (By.NAME, "age")