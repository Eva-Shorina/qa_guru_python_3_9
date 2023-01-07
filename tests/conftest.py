import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 2000
    browser.config.window_height = 1500

    yield

    browser.quit()

