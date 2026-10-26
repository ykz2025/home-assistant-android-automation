from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page object providing robust Explicit Waits (WebDriverWait)."""

    def __init__(self, driver, timeout: int = 25):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator: tuple):
        """Waits for element visibility and returns it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        """Waits until the element is clickable and performs click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def set_text(self, locator: tuple, text: str):
        """Clears input field, enters text, and hides soft keyboard."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

    def wait_for_element_visible(self, locator: tuple) -> bool:
        """Explicitly waits for element visibility on screen until timeout."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
