from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.mark.parametrize(["width", "height"], [(1980, 1024), (900, 600)], ids=["Desktop", "Mobile"])
def test_parametrized(width, height):
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('/')
    if (width == 1980) and (height == 1024):
        s(".HeaderMenu-link--sign-in").click()
    elif (width == 900) and (height == 600):
        s(".Button-label").click()
        s(".HeaderMenu-link--sign-in").click()
    else:
        pytest.fail("Full hd is unsuitable for mobile")
