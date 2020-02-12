import unittest
from selenium import webdriver
import page

class ChildrenInputsNumber(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.booking.com")

    def test_show_price(self):
        # load main and result page
        main_page = page.MainPage(self.driver)
        results_page = page.ResultPage(self.driver) 

        # choose first city from the menu below
        main_page.chose_city()
        
        # checking the opening of the hotel listing page
        assert results_page.is_hotels_open(), 'No hotels found.'

        # check opening calendar 
        assert results_page.is_calendar_open(), 'Calendar is not opened.'
          
        # check on the contain of the reservation price or reservation status
        assert results_page.check_status(), 'Page contains the reservation price or reservation status.'

        # Click "show prices" button for first hotel
        main_page.click_show_price()

        # check opening calendar 
        assert results_page.is_calendar_open(), 'Calendar is not opened.'

        # set dates in   
        main_page.set_check_in()

        # Submit search form
        main_page.search()

        # checking result 
        assert (not results_page.check_status()), 'Page contains the reservation price or reservation status.'


    def tearDown(self):
        self.driver.quit() 

    
if __name__ == "__main__":
    unittest.main()    