from selenium import webdriver
from TripAdvisorPages.HomePage import *


def test_logo_redirection():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.tripadvisor.com')
    driver.find_element(*logo).click()
    actual_url = driver.current_url
    assert 'https://www.tripadvisor.in' in actual_url

