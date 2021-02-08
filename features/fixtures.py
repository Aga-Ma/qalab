from selenium import webdriver
from behave.fixture import fixture


@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome("C:/drivers/chromedriver.exe")
    context.driver.implicitly_wait(10)
    yield context.driver
    context.driver.quit()
