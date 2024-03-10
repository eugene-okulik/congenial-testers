from selenium.webdriver.common.by import By


SELECT_PER_PAGE = (By.CSS_SELECTOR, '#limiter')
ITEMS = (By.CSS_SELECTOR, '.item.product.product-item')
BUTTON_COMPARE = (By.CSS_SELECTOR, 'a.action.tocompare')
COMPARE_LIST = (By.CSS_SELECTOR, '.product-item.odd.last')
COMPARE_ITEM = (By.CSS_SELECTOR, '.product-item-name')
SORT_BLOCK = (By.CSS_SELECTOR, '#narrow-by-list')
SORT_BY = (By.XPATH, f"//div[contains(text(), 'Style')]")
SORT_COUNT = (By.CSS_SELECTOR, '.count')
