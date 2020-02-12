from locators import MainPageLocators
from locators import SearchResultsPageLocators
import datetime


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def chose_city(self):
        city = self.driver.find_element(*MainPageLocators.CITY)
        city.click()
 
    def click_show_price(self):
        show_price = self.driver.find_element(*MainPageLocators.SHOW_PRICE)
        show_price.click()
    
    def set_check_in(self):
        check_in = self.driver.find_elements(*MainPageLocators.CHECK_IN)
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).day
        for day in check_in:
            if day.text == str(tomorrow):
                day.click()
                break

    def search(self):
        search = self.driver.find_element(*MainPageLocators.SEAERCH) 
        search.click()   
        
                
class ResultPage(BasePage):
    def is_hotels_open(self):
        hotel = self.driver.find_elements(*SearchResultsPageLocators.HOTELS)
        return hotel

    def is_calendar_open(self):
        calendar = self.driver.find_element(*SearchResultsPageLocators.CALENDAR)
        return calendar.is_displayed()

    def check_status(self):
        status = self.driver.find_element(*SearchResultsPageLocators.CHECK_STATUS)
        return (not status.text.strip())
    
    