
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class Booking_report:
    def __init__(self, hotel_boxes:WebElement):
        self.hotel_boxes = hotel_boxes

    def pull_title(self):
        i = 0
        while i < len(self.hotel_boxes):
            all_hotel_names =  self.hotel_boxes[i].find_element(
                by=By.CSS_SELECTOR,
                value='div[data-testid="title"]'
            ).get_attribute("innerHTML").strip()
            print(all_hotel_names)
            i+=1