import os

import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def desktop_resolution():
    browser.config.window_width = 1980
    browser.config.window_height = 1024


@pytest.fixture(scope='function')
def mobile_resolution():
    browser.config.window_width = 900
    browser.config.window_height = 600


@pytest.fixture(scope='function')
def application(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://github.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (os.getenv('selene.hold_browser_open', 'false').lower() == 'true')
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    yield
    browser.quit()
