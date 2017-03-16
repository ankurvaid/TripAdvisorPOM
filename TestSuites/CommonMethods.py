from selenium import webdriver

def initialize():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tripadvisor.in")
    return driver