from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import booking.constants as const
from selenium.webdriver.common.by import By
from booking.booking_filtre import Bookingfiltre
import time
from booking.BookingReport import Booking_report
from selenium.webdriver.remote.webelement import WebElement


class Booking (webdriver.Chrome):
    def __init__(self, teardown = False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #ignore devtools message
        super(Booking, self).__init__(options=options)
    def __exit__(self, *args):
        if self.teardown:
            self.quit()


    def land_first_page (self):
        self.get(const.BASE_URL)
        self.implicitly_wait(8)
        self.maximize_window()

    def refuse_cookie (self):
        try:
            cookie_refuse = WebDriverWait(self, 5).until(
            EC.element_to_be_clickable(
            (By.ID, "onetrust-reject-all-handler")
            )
            )
            cookie_refuse.click()
        except:
            print("no cookie bar")
    
    def change_currency(self, currency =None):
        currency_menu = self.find_element(
            by=By.CSS_SELECTOR,
            value='button[data-modal-header-async-type="currencyDesktop"]'
        )
        currency_menu.click()
        seleted_currency = self.find_element(
            by=By.CSS_SELECTOR,
            value = f'a[data-modal-header-async-url-param*="selected_currency={currency.upper()}"'
        )
        seleted_currency.click()
    def place_to_go(self, place = None):
        place_field = self.find_element(by=By.ID, value='ss')
        place_field.clear()
        place_field.click()
        place_field.send_keys(place)
        selected_place = self.find_element(by=By.CSS_SELECTOR, value='li[data-i="0"]')
        selected_place.click()
    def select_when(self, check_in, check_out):
        check_in_field = self.find_element(by=By.CSS_SELECTOR, value=f'td[data-date="{check_in}"]')
        check_in_field.click()
        check_out_field = self.find_element(by=By.CSS_SELECTOR, value=f'td[data-date="{check_out}"]')
        check_out_field.click()

    def select_guest(self, nombre_adult):
        guest_field = self.find_element(by=By.ID, value="xp__guests__toggle" )
        guest_field.click()
        adult_moins = self.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Supprimer des Adultes"]')
        current_adult =int(self.find_element(by=By.ID, value= "group_adults").get_attribute("value").strip()) 
        # diminuer le nombre d'adult à 1
        x = 1
        while x < current_adult:
            adult_moins.click()
            x+=1

       # augmenter le nombre d'adult à nombre_adult
        adult_plus = self.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Ajouter des Adultes"]')
     
        for _ in range(nombre_adult -1):
            adult_plus.click()
    
    def submit_search(self):
        search_button = self.find_element(by=By.CSS_SELECTOR, value='button[data-sb-id="main"]')
        search_button.click()

    def applyfilter(self):
        filtre = Bookingfiltre(driver=self)
        filtre.apply_star_rate(3,4,5)
        time.sleep(2)
        filtre.apply_lowest_price_first()
    
    def report_result(self):
        time.sleep(3)
        all_hotels = self.find_element(
            by=By.ID, 
            value="search_results_table"
            ).find_elements(
        by=By.CSS_SELECTOR, 
        value='div[data-testid="property-card"]'
        )
        report = Booking_report(all_hotels)
        report.pull_title()

       

  
      #  single_hotel_array = all_hotels.find_elements(by=By.CSS_SELECTOR, value='div[data-testid="property-card"]')
      #  report = Booking_report(all_hotels)
       # report.pull_title()
        


           
    



        