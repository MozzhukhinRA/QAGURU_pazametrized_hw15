import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config_open():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options


@pytest.fixture(params=[(1920, 1080), (1280, 1220), (740, 800), (575, 660)])
def setup_browser(request):
    height, width = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    if height > 1000:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()


@pytest.fixture(params=[(1920, 1080), (1280, 1220)])
def size_desktop(request):
    height, width = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()


@pytest.fixture(params=[(740, 800), (575, 660)])
def size_mobile(request):
    height, width = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()
