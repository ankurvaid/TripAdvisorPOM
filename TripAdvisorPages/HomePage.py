from selenium.webdriver.common.by import By

logo = (By.CSS_SELECTOR, "span.topLogo>a.logoWrap>img.svg-taLogo")
find_search_box = (By.ID, "mainSearch")
near_search_box = (By.ID, "GEO_SCOPED_SEARCH_INPUT")
search_button = (By.CSS_SELECTOR, "button#SEARCH_BUTTON>div#SEARCH_BUTTON_CONTENT div.inner")
search_dropdown_hotels = (By.CSS_SELECTOR, "span.poi-name.primaryText.no-geo>span.poi_overview_item")
search_dropdown_rajasthan = (By.CSS_SELECTOR, "li.displayItem.result.selected span.poi-name.primaryText>b")
