
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class Booking_report:
    def __init__(self, hotel_boxes:WebElement):
        self.hotel_boxes = hotel_boxes

    def pull_hotels_infos(self):
        collection =[]
        i = 0
        while i < len(self.hotel_boxes):
            # get hotel name
            hotel_name =  self.hotel_boxes[i].find_element(
                by=By.CSS_SELECTOR,
                value='div[data-testid="title"]'
            ).get_attribute("innerHTML").strip()
            # get hotel price
            hotel_price = self.hotel_boxes[i].find_element(
                by=By.CSS_SELECTOR,
                value= 'div[data-testid="price-and-discounted-price"]'
            ).find_element(
                by=By.TAG_NAME,
                value='span'
            ).get_attribute("innerHTML").strip()
            # get hotel score
            try:
                hotel_score = self.hotel_boxes[i].find_element(
                by=By.CSS_SELECTOR,
                value='div[aria-label*="Avec une note de"]'
                ).get_attribute("innerHTML").strip()
            except:
                hotel_score = "no score"
            collection.append([hotel_name,hotel_score, hotel_price])
            i+=1
        print(collection)
