from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.mark.parametrize("application", [(900, 600), (1980, 1024)], indirect=True)
def test_parametrized_indirect(application):
    if (browser.config.window_width != 900) and (browser.config.window_height != 600):
        pytest.skip("Full HD is unsuitable for mobile tests")
    browser.open('/')
    s(".Button-label").click()
    s(".HeaderMenu-link--sign-in").click()
