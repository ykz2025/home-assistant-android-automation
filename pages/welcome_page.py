from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class WelcomePage(BasePage):
    """Сторінка початкового налаштування та підключення сервера Home Assistant."""

    # 1. Головна кнопка на першому вітальному екрані
    BTN_CONNECT_SERVER = (
        AppiumBy.CLASS_NAME,
        "android.widget.Button"
    )

    # 2. Посилання ручного вводу адреси
    LNK_ENTER_MANUALLY = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Enter address manually")'
    )

    # 3. Поле вводу адреси
    INPUT_SERVER_URL = (
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    # 4. Кнопка Connect
    BTN_SUBMIT_CONNECT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Connect")'
    )

    # 5. Текст помилки валідації
    LBL_ERROR_MESSAGE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Invalid")'
    )

    # 6. Кнопка Back на екрані результату 'Unable to connect'
    BTN_BACK_ON_ERROR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Back")'
    )

    # Бізнес-методи
    def start_manual_connection(self):
        """Перехід від початкового екрана до ручного введення адреси сервера."""
        self.click(self.BTN_CONNECT_SERVER)
        self.click(self.LNK_ENTER_MANUALLY)

    def enter_server_url(self, url: str):
        """Введення адреси сервера у поле URL зі схованням клавіатури."""
        self.set_text(self.INPUT_SERVER_URL, url)

    def submit_connection(self):
        """Клік по кнопці підтвердження підключення."""
        self.click(self.BTN_SUBMIT_CONNECT)

    def is_connect_button_disabled(self) -> bool:
        """Перевіряє, чи стала кнопка Connect неактивною через невалідний ввід."""
        try:
            element = self.find(self.BTN_SUBMIT_CONNECT)
            return element.get_attribute("enabled") == "false"
        except Exception:
            return False

    def is_error_message_displayed(self) -> bool:
        """Очікує та перевіряє появу повідомлення про невалідну адресу."""
        return self.wait_for_element_visible(self.LBL_ERROR_MESSAGE)

    def is_unable_to_connect_displayed(self) -> bool:
        """Очікує та перевіряє появу екрана результату підключення (кнопка Back)."""
        return self.wait_for_element_visible(self.BTN_BACK_ON_ERROR)
