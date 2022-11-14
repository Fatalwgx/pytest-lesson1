from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_desktop(desktop_resolution):
    browser.open('/')
    s(".HeaderMenu-link--sign-in").click()


def test_mobile(mobile_resolution):
    browser.open('/')
    s(".Button-label").click()
    s(".HeaderMenu-link--sign-in").click()
