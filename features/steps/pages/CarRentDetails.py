from selenium.webdriver.common.by import By

from .BasePage import BasePage


class DetailsPage(BasePage):

    def __init__(self, context):
        super().__init__(context.driver)

    @property
    def model(self):
        return self.driver.find_element(By.XPATH, "//div[@class='card-header']")

    @property
    def company(self):
        return self.driver.find_element(By.XPATH, "//*[@class='card-title']")

    @property
    def price_per_day(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Price per day:')]")

    @property
    def location(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Location:')]")

    @property
    def license_plate(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'License plate:')]")

    @property
    def pick_up_date(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Pickup date:')]")

    @property
    def drop_off_date(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Dropoff date:')]")

    @property
    def rent(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Rent!')]")
