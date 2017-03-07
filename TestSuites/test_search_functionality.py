from selenium import webdriver
from TripAdvisorPages.HomePage import *
from TripAdvisorPages.RajasthanHotelsPage import *

def test_valid_hotel_search_text_input():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.tripadvisor.com')
    driver.find_element(*find_search_box).send_keys("hotel")
    driver.find_element(*near_search_box).send_keys("rajasthan")
    driver.find_element(*search_button).click()
    welcome_text = driver.find_element(*welcome_message).text
    assert welcome_text == "Rajasthan Hotels"