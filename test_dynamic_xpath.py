import pytest
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.guvi.in/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_relative_xpath_parent_child(driver):

    pass
