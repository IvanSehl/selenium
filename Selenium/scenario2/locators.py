from selenium.webdriver.common.by import By

class MainPageLocators(object):
    CITY = (By.CLASS_NAME, "unified-postcard")
    SHOW_PRICE = (By.CLASS_NAME, "txp-cta")
    CHECK_IN = (By.CLASS_NAME, "c2-day-inner")
    SEAERCH = (By.CLASS_NAME, "sb-searchbox__button")

class SearchResultsPageLocators(object):
    HOTELS = (By.CLASS_NAME, "sr_item") 
    CALENDAR = (By.XPATH, "/html/body/div[3]/div/div[3]/div[3]/div[2]/div[1]/div[1]/form/div[3]/div/div[2]/div")    
    CHECK_STATUS = (By.CLASS_NAME, "sr_rooms_table_block")    