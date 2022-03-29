from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .setupDriver import SetUpDriver


class BaseAutomationTools:
    def __init__(self):
        self.driver = SetUpDriver.driver_constructor()

    def safe_get(self, url: str):
        self.driver.set_page_load_timeout(30)
        try:
            self.driver.get(url)
        except TimeoutException:
            self.driver.refresh()

    def element_existence(self, elementloc, findBy: By, condition: expected_conditions):
        try:
            return self.driver.find_element(by=findBy, value=elementloc)
        except (TimeoutException, NoSuchElementException):
            return WebDriverWait(self.driver, 10).until(condition((findBy, elementloc)))

    def close_browser(self):
        self.driver.close()
        self.driver.quit()
