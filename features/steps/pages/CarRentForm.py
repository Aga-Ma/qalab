from selenium.webdriver.common.by import By

from .BasePage import BasePage


class SummaryPage(BasePage):

    def __init__(self, context):
        super().__init__(context.driver)

    @property
    def name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='name']")

    @property
    def last_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='last_name']")

    @property
    def card_number(self):
        return self.driver.find_element(By.XPATH, "//input[@id='card_number']")

    @property
    def email(self):
        return self.driver.find_element(By.XPATH, "//input[@name='email']")

    def fill_name(self, user_name):
        self.name.send_keys(user_name)

    def fill_last_name(self, user_last_name):
        self.last_name.send_keys(user_last_name)

    def fill_card_number(self, ca_num):
        self.card_number.send_keys(ca_num)

    def fill_email(self, email_address):
        self.email.send_keys(email_address)

    @property
    def rent(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), 'Rent')]")

    def alert(self, text):
        return self.driver.find_element(By.XPATH, "//*[contains(text(), '{text}')]".format(text=text))
