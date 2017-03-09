from selenium.webdriver.common.by import By

logo = (By.CSS_SELECTOR, "span.topLogo>a.logoWrap>img.svg-taLogo")
find_search_box = (By.ID, "mainSearch")
near_search_box = (By.ID, "GEO_SCOPED_SEARCH_INPUT")
search_button = (By.CSS_SELECTOR, "button#SEARCH_BUTTON>div#SEARCH_BUTTON_CONTENT div.inner")
search_auto_suggest_hotels = (By.CSS_SELECTOR, "span.poi-name.primaryText.no-geo>span.poi_overview_item")
search_auto_suggest_rajasthan = (By.CSS_SELECTOR, "li.displayItem.result.selected span.poi-name.primaryText>b")
search_auto_suggest_holiday_rentals = (By.CSS_SELECTOR, "ul.resultContainer.overview>li:nth-child(2)>span>span")
search_auto_suggest_pune = (By.CSS_SELECTOR, "ul.resultContainer.local>li span>b")
header_link_login = (By.CSS_SELECTOR, "ul.options>li:nth-child(4)>span")
continue_with_facebbok_button_login = (By.CSS_SELECTOR, "div.flex_container>span.textContainer")

