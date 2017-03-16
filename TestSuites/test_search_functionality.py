from time import sleep
from TestSuites.CommonMethods import *
from TripAdvisorPages.HomePage import *
from TripAdvisorPages.PuneHolidayRentals import *
from TripAdvisorPages.RajasthanHotelsPage import *

def test_valid_hotel_search_text_input():
    driver = initialize()
    driver.find_element(*find_search_box).click()
    driver.find_element(*find_search_box).send_keys("hotels")
    driver.find_element(*near_search_box).click()
    sleep(1)
    driver.find_element(*near_search_box).send_keys("rajasthan")
    sleep(2)
    driver.find_element(*search_button).click()
    welcome_text = driver.find_element(*welcome_message).text
    assert welcome_text == "Rajasthan Hotels"

def test_valid_hotel_search_auto_suggestion():
    driver = initialize()
    driver.find_element(*find_search_box).click()
    sleep(2)
    driver.find_element(*search_auto_suggest_hotels).click()
    driver.find_element(*near_search_box).click()
    driver.find_element(*near_search_box).send_keys("rajasthan")
    sleep(2)
    driver.find_element(*search_auto_suggest_rajasthan).click()
    driver.find_element(*search_button).click()
    welcome_text = driver.find_element(*welcome_message).text
    assert welcome_text == "Rajasthan Hotels"

def test_valid_hotel_rentals_search_auto_suggestion():
    driver = initialize()
    driver.find_element(*find_search_box).click()
    sleep(2)
    driver.find_element(*search_auto_suggest_holiday_rentals).click()
    driver.find_element(*near_search_box).click()
    driver.find_element(*near_search_box).send_keys("pune")
    sleep(2)
    driver.find_element(*search_auto_suggest_pune).click()
    driver.find_element(*search_button).click()
    welcome_text = driver.find_element(*welcome_message).text
    assert welcome_text == "Holiday Rentals in Pune, India"



