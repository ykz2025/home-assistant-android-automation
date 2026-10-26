from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class WelcomePage(BasePage):
    """Page Object for Home Assistant initial setup and server connection screen."""

    # 1. Main action button on welcome screen
    BTN_CONNECT_SERVER = (
        AppiumBy.CLASS_NAME,
        "android.widget.Button"
    )

    # 2. Text link for manual server URL entry
    LNK_ENTER_MANUALLY = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Enter address manually")'
    )

    # 3. Server address input field
    INPUT_SERVER_URL = (
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    # 4. Connect button
    BTN_SUBMIT_CONNECT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Connect")'
    )

    # 5. Validation error label
    LBL_ERROR_MESSAGE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Invalid")'
    )

    # 6. Back button on 'Unable to connect' result screen
    BTN_BACK_ON_ERROR = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Back")'
    )

    # Business Actions
    def start_manual_connection(self):
        """Navigate from welcome screen to manual address entry."""
        self.click(self.BTN_CONNECT_SERVER)
        self.click(self.LNK_ENTER_MANUALLY)

    def enter_server_url(self, url: str):
        """Enter server address into URL input field and hide keyboard."""
        self.set_text(self.INPUT_SERVER_URL, url)

    def submit_connection(self):
        """Click connection confirmation button."""
        self.click(self.BTN_SUBMIT_CONNECT)

    def is_connect_button_disabled(self) -> bool:
        """Check whether Connect button is disabled due to invalid input."""
        try:
            element = self.find(self.BTN_SUBMIT_CONNECT)
            return element.get_attribute("enabled") == "false"
        except Exception:
            return False

    def is_error_message_displayed(self) -> bool:
        """Wait for and verify that invalid URL error message is visible."""
        return self.wait_for_element_visible(self.LBL_ERROR_MESSAGE)

    def is_unable_to_connect_displayed(self) -> bool:
        """Wait for and verify 'Unable to connect' result screen (Back button visible)."""
        return self.wait_for_element_visible(self.BTN_BACK_ON_ERROR)
