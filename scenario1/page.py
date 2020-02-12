from locators import MainPageLocators
from locators import SearchResultsPageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def is_title_matches(self):
        return "Booking.com |" in self.driver.title

    def click_guests_field(self):
        guests = self.driver.find_element(*MainPageLocators.GUESTS_FIELD)
        guests.click()
    
    def add_child(self):
        add = self.driver.find_element(*MainPageLocators.ADD_CHILD)
        i = 0
        while i < Set_N.N:
            add.click()
            i += 1
            
class ResultPage(BasePage):
    def is_same_amount(self):
        fields_amounts = self.driver.find_elements(*SearchResultsPageLocators.FIELDS_CHILD_INPUT)
        return len(fields_amounts) == Set_N.N
      
class Set_N(object):
    N = 0