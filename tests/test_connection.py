import pytest
from pages.welcome_page import WelcomePage


class TestHomeAssistantConnection:
    """Test suite covering initial server connection flows in Home Assistant Android."""

    def test_validation_invalid_server_url(self, driver):
        """
        Test 1 (Negative): Validation of invalid server address format.
        
        Steps:
        1. Navigate to manual server address input.
        2. Enter invalid string 'invalid'.
        3. Verify form validation (either disabled Connect button or visible error message).
        """
        welcome_page = WelcomePage(driver)

        # 1. Start manual connection flow
        welcome_page.start_manual_connection()

        # 2. Enter invalid URL
        welcome_page.enter_server_url("invalid")

        # 3. Assert validation response (error displayed or button disabled)
        has_error = welcome_page.is_error_message_displayed()
        is_disabled = welcome_page.is_connect_button_disabled()
        
        assert has_error or is_disabled, (
            "Form did not react to invalid URL: no error displayed and Connect button remains active!"
        )

    def test_positive_server_connection_flow(self, driver):
        """
        Test 2 (Positive): Connection attempt to valid demo server URL.
        
        Steps:
        1. Navigate to manual server address input.
        2. Enter valid URL 'https://demo.home-assistant.io'.
        3. Click 'Connect' button.
        4. Verify navigation to connection result screen.
        """
        welcome_page = WelcomePage(driver)

        # 1. Start manual connection flow
        welcome_page.start_manual_connection()

        # 2. Enter valid server URL
        welcome_page.enter_server_url("https://demo.home-assistant.io")

        # 3. Submit connection
        welcome_page.submit_connection()

        # 4. Assert navigation to connection result screen
        assert welcome_page.is_unable_to_connect_displayed(), (
            "Expected connection result screen did not appear!"
        )
