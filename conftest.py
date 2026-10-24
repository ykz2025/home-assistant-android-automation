import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    """Фікстура ініціалізації та запуску додатку перед кожним тестом."""
    app_package = "io.homeassistant.companion.android.minimal"
    app_activity = "io.homeassistant.companion.android.launch.LaunchActivity"

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = app_package
    options.app_activity = app_activity
    options.no_reset = True
    
    # Таймаути
    options.set_capability("appium:newCommandTimeout", 300)
    options.set_capability("appium:uiautomator2ServerLaunchTimeout", 90000)
    options.set_capability("appium:adbExecTimeout", 60000)

    appium_server_url = "http://127.0.0.1:4723"
    app_driver = webdriver.Remote(appium_server_url, options=options)

    # Примусовий чистий старт додатку на передній план
    app_driver.execute_script("mobile: terminateApp", {"appId": app_package})
    app_driver.execute_script("mobile: activateApp", {"appId": app_package})

    yield app_driver

    # Закриваємо сесію
    app_driver.quit()
