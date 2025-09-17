import pytest
from selene import browser, be

@pytest.mark.parametrize('size_desktop', [(1280, 1220)], indirect=True)
def test_desktop_size_git(size_desktop):
    browser.open('https://github.com')
    browser.element('[href="/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home"]').should(be.visible).click()

@pytest.mark.parametrize('size_mobile', [(575, 660)], indirect=True)
def test_mobile_size_git(size_mobile):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-toggle-bar').should(be.visible).click()
    browser.element('.HeaderMenu-button').should(be.visible).click()