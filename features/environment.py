import os
import time

from behave import use_fixture
from behave.log_capture import capture

from fixtures import browser_chrome

BEHAVE_DEBUG_ON_ERROR = True


def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context)


@capture
def after_scenario(context, scenario):
    """
    Takes screenshot if scenario fails
    """
    if context.scenario.status == 'failed':
        scenario_error_dir = os.path.join('./', 'feature_errors')
        os.makedirs(scenario_error_dir, exist_ok=True)
        scenario_file_path = os.path.join(scenario_error_dir, context.scenario.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.png')
        context.driver.save_screenshot(scenario_file_path)
