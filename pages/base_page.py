from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовий клас сторінки з явними очікуваннями WebDriverWait."""

    def __init__(self, driver, timeout: int = 25):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator: tuple):
        """Очікує видимість елемента та повертає його."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        """Очікує клікабельність елемента і виконує клік."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def set_text(self, locator: tuple, text: str):
        """Очищує поле, вводить текст і приховує віртуальну клавіатуру."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

    def wait_for_element_visible(self, locator: tuple) -> bool:
        """Явно очікує видимість елемента на екрані до закінчення таймауту."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
