import re
import datetime

from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException

from features.steps.pages import *

NAME = 'James'
LAST_NAME = 'Bond'
CARD_NUMBER = '007'
INVALID_CARD_NUMBER = 'abc'
EMAIL = 'bond@jamesbond.com'
INVALID_EMAIL = 'bondjamesbond.com'


class PageNotAvailable(Exception):
    """Raised if expected page is not reached"""
    pass


class ResultsDoesNotMatchSearchCriteria(Exception):
    """Raised if return search results doesn't match search criteria"""
    pass


@given('a user visit car rent search page')
def step_impl(context):
    page = SearchPage(context)
    page.load('http://qalab.pl.tivixlabs.com/')


@given('a user enters all data on car rent search page')
def step_impl(context):
    today = datetime.date.today()
    pickup_date = today.strftime("%d.%m.%Y")
    dropoff_date = today + datetime.timedelta(7)
    dropoff_date = dropoff_date.strftime("%d.%m.%Y")
    context.execute_steps(u"""
                given a user visit car rent search page
                when a user choose the "{country}" and "{city}"
                when a user gives car model "{model}"
                when a user chose pickup date "{pickup_date}"
                when a user chose drop-off date "{dropoff_date}"
                when a user click the search button
            """.format(country="Poland", city="Cracow", model="Alfa Romeo",
                       pickup_date=pickup_date, dropoff_date=dropoff_date))


@given('a user searched for a car to rent')
def step_impl(context):
    context.execute_steps(u"""
                given a user enters all data on car rent search page
                when a user click the Rent button
                and the rent details page is displayed""")


@given('a user goes to rent form')
def step_impl(context):
    page = DetailsPage(context)
    page.rent.click()


@when('a user gives car model "{model}"')
def step_impl(context, model):
    page = SearchPage(context)
    page.insert_model(model)


@when('a user chose pickup date "{pickup_date}"')
def step_impl(context, pickup_date):
    page = SearchPage(context)
    page.set_pick_up_date(pickup_date)


@when('a user chose drop-off date "{dropoff_date}"')
def step_impl(context, dropoff_date):
    page = SearchPage(context)
    page.set_drop_off_date(dropoff_date)


@step('dates fields are empty')
def step_impl(context):
    page = SearchPage(context)
    pickup_date = page.pick_up_date.text
    dropoff_date = page.drop_off_date.text
    if pickup_date or dropoff_date:
        context.failed = True


@when('a user click the Rent button')
def step_impl(context):
    page = SearchPage(context)
    page.rent.click()


@when('a user enters the personal data')
def step_impl(context):
    page = SummaryPage(context)
    page.fill_name(NAME)
    page.fill_last_name(LAST_NAME)
    page.fill_card_number(CARD_NUMBER)
    page.fill_email(EMAIL)


@when('a user enters last name, card number and email')
def step_impl(context):
    page = SummaryPage(context)
    page.fill_last_name(NAME)
    page.fill_card_number(CARD_NUMBER)
    page.fill_email(EMAIL)


@when('a user enters name, card number and email')
def step_impl(context):
    page = SummaryPage(context)
    page.fill_name(NAME)
    page.fill_card_number(CARD_NUMBER)
    page.fill_email(EMAIL)


@when('a user enters name, last name and email')
def step_impl(context):
    page = SummaryPage(context)
    page.fill_name(NAME)
    page.fill_last_name(LAST_NAME)
    page.fill_email(EMAIL)


@when('a user enters name, last name and card number')
def step_impl(context):
    page = SummaryPage(context)
    page.fill_name(NAME)
    page.fill_last_name(LAST_NAME)
    page.fill_card_number(CARD_NUMBER)


@when('a user enters name, last name, card number and invalid email')
def step_impl(context):
    page = SummaryPage(context)
    page.fill_name(NAME)
    page.fill_last_name(LAST_NAME)
    page.fill_card_number(CARD_NUMBER)
    page.fill_email(INVALID_EMAIL)


@when('a user enters name, last name, invalid card number and email')
def step_impl(context):
    page = SummaryPage(context)
    page.fill_name(NAME)
    page.fill_last_name(LAST_NAME)
    page.fill_card_number(INVALID_CARD_NUMBER)
    page.fill_email(EMAIL)


@when('a user click rent')
def step_impl(context):
    page = SummaryPage(context)
    page.rent.click()


@then('alert "{alert}" is displayed')
def step_impl(context, alert):
    page = SummaryPage(context)
    page.alert(alert)


@step('a user fill in required date fields: "{pickup}", "{dropoff}"')
def step_impl(context, pickup, dropoff):
    context.execute_steps(u"""
                when a user chose pickup date "{pickup_date}"
                when a user chose drop-off date "{dropoff_date}"
            """.format(pickup_date=pickup, dropoff_date=dropoff))


@step('a user click the search button')
def step_impl(context):
    page = SearchPage(context)
    page.search_button.click()


@step('a user choose the "{country}" and "{city}"')
def step_impl(context, country, city):
    page = SearchPage(context)
    page.select_country(country)
    page.select_city(city)


@step('results table is displayed')
def step_impl(context):
    page = SearchPage(context)
    page.results()


@step('the rent details page is displayed')
def step_impl(context):
    rent_car_details_url = r"http:\/\/qalab.pl.tivixlabs.com\/details\/\d+"
    if not re.match(rent_car_details_url, context.driver.current_url):
        raise PageNotAvailable


@then('missing date fields alert is displayed')
def step_impl(context):
    page = SearchPage(context)
    page.alert('Please fill pickup and drop off dates')


@then('date fields alert is displayed')
def step_impl(context):
    page = SearchPage(context)
    page.alert('Please enter a valid date!')


@then('results table isn\'t displayed')
def step_impl(context):
    page = SearchPage(context)
    try:
        page.results()
    except NoSuchElementException:
        pass


@then('the result table shows the expected model "{model}" for rent')
def step_impl(context, model):
    page = SearchPage(context)
    if model not in page.results():
        raise ResultsDoesNotMatchSearchCriteria


@then('car details are available')
def step_impl(context):
    page = DetailsPage(context)
    page.model
    page.company
    page.price_per_day
    page.location
    page.license_plate
    page.pick_up_date
    page.drop_off_date
    page.rent


@then('car rent is successful')
def step_impl(context):
    """
    WARNING! This step implementation cannot be considered as proper car rent validation.
    Below implementation is due to unknown requirements.
    """
    if ("Page not found" or "Exception") in context.driver.page_source:
        raise PageNotAvailable
