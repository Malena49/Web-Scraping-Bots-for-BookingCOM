from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Bookingfiltre:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    def apply_star_rate(self, *star_values):
        for star_value in star_values:
            start_element = self.driver.find_element(by=By.CSS_SELECTOR, value=f'div[data-filters-item="class:class={star_value}"]')
            start_element.click()
            

    def apply_lowest_price_first (self):
     
        lowest_price = self.driver.find_element(by=By.CSS_SELECTOR, value='a[data-type="price"]')
        lowest_price.click()