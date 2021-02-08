from selenium.webdriver.common.by import By

from .BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, context):
        super().__init__(context.driver)

    @property
    def country(self):
        return self.driver.find_element(By.XPATH, "//select[@name='country']]")

    @property
    def city(self):
        return self.driver.find_element(By.XPATH, "//select[@name='city']]")

    @property
    def model(self):
        return self.driver.find_element(By.XPATH, "//input[@name='model']")

    @property
    def pick_up_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='pickup']")

    @property
    def drop_off_date(self):
        return self.driver.find_element(By.XPATH, "//input[@name='dropoff']")

    def select_country(self, name):
        xpath = "//select[@name='country']/option[text()='{option}']".format(option=name)
        self.driver.find_element(By.XPATH, xpath).click()

    def select_city(self, name):
        xpath = "//select[@name='city']/option[text()='{option}']".format(option=name)
        self.driver.find_element(By.XPATH, xpath).click()

    def insert_model(self, value):
        self.model.send_keys(value)

    def set_pick_up_date(self, date):
        self.pick_up_date.send_keys(date)

    def set_drop_off_date(self, date):
        self.drop_off_date.send_keys(date)

    def alert(self, text):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), '{text}')]".format(text=text))

    @property
    def search_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")

    def results(self):
        return self.driver.find_element(By.XPATH, "//table[@id='search-results']")

    @property
    def rent(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Rent')]")
