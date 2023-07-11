import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope="module")
def maximize_browser_window():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_google_search(maximize_browser_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_no_results(maximize_browser_window):
    browser.open('https://google.com')
    random_string = 'glfnbhfgnhoklbmftgyphjpofmkbnmgkbmkghnkdmbdmgkhmfjodkro[tgkrdkjhibjmpoxdbhpiniet'
    browser.element('[name="q"]').should(be.blank).type(random_string).press_enter()
    browser.element('[id="topstuff"]').should(have.text(f'По запросу {random_string} ничего не найдено.'))



