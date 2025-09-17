import pytest
from selene import browser, be

from conftest import setup_browser


def test_desktop_size_git(setup_browser):
    if setup_browser != 'desktop':
        pytest.skip('Окно браузера не соответствует разрешению устройства (desktop)')
    browser.open('https://github.com')
    browser.element('[href="/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home"]').should(be.visible).click()

def test_mobile_size_git(setup_browser):
    if setup_browser != 'mobile':
        pytest.skip('Окно браузера не соответствует разрешению устройства (mobile)')
    browser.open('https://github.com')
    browser.element('.HeaderMenu-toggle-bar').should(be.visible).click()
    browser.element('.HeaderMenu-button').should(be.visible).click()