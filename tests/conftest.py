import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.driver.maximize_window()
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
