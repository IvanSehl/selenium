import unittest
from selenium import webdriver
import page

class ChildrenInputsNumber(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.booking.com")

    def test_inputs_number(self):
        # set the number of children
        page.Set_N.N = 5
        
        # load main and result pages
        main_page = page.MainPage(self.driver)
        result_page = page.ResultPage(self.driver)
        
        # Checks if the word "Booking.com |" is in title
        assert main_page.is_title_matches, "It's not a home page." 

        # open menu for selecting strangers number
        main_page.click_guests_field()

        # add number of children up to N
        main_page.add_child()
        
        # check result    
        result = page.ResultPage(self.driver)
        assert result.is_same_amount(), "Amount of input fields not equal N"

    def tearDown(self):
        self.driver.quit()    

if __name__ == "__main__":
    unittest.main()