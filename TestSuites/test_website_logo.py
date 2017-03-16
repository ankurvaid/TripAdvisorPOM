from TripAdvisorPages.HomePage import *
from TestSuites.CommonMethods import *


def test_logo_redirection():
    driver = initialize()
    driver.find_element(*logo).click()
    actual_url = driver.current_url
    assert 'https://www.tripadvisor.in' in actual_url

