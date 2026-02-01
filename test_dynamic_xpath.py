import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    yield driver
    driver.quit()


def test_relative_xpath_and_axes(setup):
    driver = setup

    menu_items = driver.find_elements(
        By.XPATH, "//p[contains(@class,'menu-hover')]"
    )

    for item in menu_items:
        # Parent
        parent = item.find_element(By.XPATH, "./parent::div")

        # First child
        first_child = parent.find_element(By.XPATH, "./*[1]")

        # Second sibling (if any)
        second_sibling = item.find_elements(
            By.XPATH, "./parent::div/following-sibling::*[2]"
        )

        assert parent is not None
        assert first_child is not None

    # Parent of element with href
    href_parents = driver.find_elements(
        By.XPATH, "//*[@href]/parent::*"
    )
    assert len(href_parents) > 0

    # Axes
    ancestors = driver.find_elements(
        By.XPATH, "//p[contains(@class,'menu-hover')]/ancestor::*"
    )
    following_siblings = driver.find_elements(
        By.XPATH,
        "//p[contains(@class,'menu-hover')]/parent::div/following-sibling::*"
    )
    preceding_elements = driver.find_elements(
        By.XPATH, "//p[contains(@class,'menu-hover')]/preceding::*"
    )

    assert len(ancestors) > 0
    assert len(following_siblings) > 0
    assert len(preceding_elements) > 0
