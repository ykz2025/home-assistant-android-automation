# Home Assistant Android - Mobile Test Automation Framework

[![Appium 2](https://img.shields.io/badge/Appium-2.x%20%2F%203.8.0-purple?style=flat&logo=appium)](https://appium.io)
[![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python)](https://python.org)
[![Pytest](https://img.shields.io/badge/Pytest-9.1.1-green?style=flat&logo=pytest)](https://docs.pytest.org)
[![UiAutomator2](https://img.shields.io/badge/Driver-UiAutomator2%208.7.0-brightgreen?style=flat&logo=android)](https://github.com/appium/appium-uiautomator2-driver)
[![Architecture](https://img.shields.io/badge/Design_Pattern-Page_Object_Model-orange?style=flat)](https://martinfowler.com/bliki/PageObject.html)

A robust mobile test automation framework designed for the native Android application **Home Assistant Companion** (`app-minimal-release.apk`).

## Overview

This project implements an end-to-end mobile automation solution using **Python**, **Appium 2**, the official **UiAutomator2** driver, and **Pytest**. Built with the **Page Object Model (POM)** pattern, it ensures clean separation of concerns, high maintainability, resilient locators, and scalable test execution against native Android UI built with Jetpack Compose.

## Target Application & Domain

- **Application:** [Home Assistant Companion for Android](https://github.com/home-assistant/android)
- **Domain:** Smart Home, Internet of Things (IoT), GreenTech & Home Energy Automation.
- **UI Architecture:** Native Android (Jetpack Compose).
- **Tested Artifact:** `app-minimal-release.apk` (API 34 / Android 14 target).

## Technologies Used

- **Python** (3.13+)
- **Appium 2** (`appium@3.8.0`) with **UiAutomator2 Driver** (`uiautomator2@8.7.0`)
- **Appium-Python-Client** (`6.0.8`) & **Selenium** (`4.51.0`)
- **Pytest** (`9.1.1`) as the core test runner and fixture provider
- **Android SDK Platform-Tools** (ADB, AVD Pixel 7a, API 34)

## Key Engineering Highlights & Best Practices

1. **Zero XPath Policy:** Complete elimination of fragile and slow absolute/relative XPaths. All element interactions use high-performance native Android selectors (`new UiSelector().textContains(...)`, `new UiSelector().className(...)`) and standard Android widget classes, achieving sub-second locator resolution.
2. **Explicit Waits Only:** Zero hardcoded delays (`time.sleep()`). All element state transitions (visibility, clickability, attribute changes) are guarded by encapsulated `WebDriverWait` handlers.
3. **Soft Keyboard & Viewport Management:** Automatic keyboard suppression (`driver.hide_keyboard()`) after text inputs prevents obscured UI elements and click interception across different screen resolutions.
4. **State Isolation:** Each test scenario executes with independent state initialization using fast app lifecycle commands (`mobile: terminateApp` and `mobile: activateApp`) rather than costly full emulator reboots or app reinstalls.

## Project Structure

```text
home-assistant-android-automation/
├── pyproject.toml          # Modern PEP 621 project configuration and dependencies
├── conftest.py             # Appium driver fixture, UiAutomator2Options, app lifecycle hooks
├── pages/
│   ├── __init__.py
│   ├── base_page.py        # BasePage encapsulating explicit waits and driver utilities
│   └── welcome_page.py     # Home Assistant onboarding Page Object (locators & business actions)
├── tests/
│   ├── __init__.py
│   └── test_connection.py  # Automated test scenarios (positive & negative flows)
├── pytest.ini              # Pytest configuration, CLI arguments, and logging settings
├── requirements.txt        # Pinned dependency manifest
├── .gitignore              # Git ignore rules for Python, IDE, and test artifacts
└── README.md               # Framework documentation
```

## Setup and Installation

### 1. Prerequisites

Ensure the following tools are installed and added to your system `PATH`:
- **Java Development Kit (JDK 17 LTS)** (`JAVA_HOME` configured)
- **Android Studio & Android SDK** (`ANDROID_HOME` and `platform-tools` in `PATH`)
- **Node.js** (v20+ LTS)

### 2. Install Appium 2 and Drivers

```powershell
npm install -g appium@latest
appium driver install uiautomator2
```

Verify the installation:
```powershell
appium driver list --installed
```

### 3. Clone and Setup Environment

```powershell
git clone https://github.com/ykz2025/home-assistant-android-automation.git
cd home-assistant-android-automation

# Option A: Modern setup via uv (recommended)
uv sync

# Option B: Standard setup via pip
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running the Tests

### 1. Start Android Emulator
Launch your configured Android Virtual Device (e.g. Pixel 7a, API 34):
```powershell
emulator -avd Pixel_7a
```
Verify the device is connected:
```powershell
adb devices
```

### 2. Start Appium Server
In a separate terminal window:
```powershell
appium
```

### 3. Execute Pytest Suite

Run all test scenarios:
```powershell
pytest -v -s
```

Run a specific test file:
```powershell
pytest -v -s tests/test_connection.py
```

Run a single test case:
```powershell
pytest -v -s -k "test_validation_invalid_server_url"
```

## Implemented Test Scenarios

| Test Case | Scenario Type | Description | Expected Status |
|:---|:---|:---|:---:|
| `test_validation_invalid_server_url` | Negative / Validation | Enters an invalid server URL (`invalid`) and verifies that the `Connect` button is disabled or an inline validation error appears. | **PASSED** |
| `test_positive_server_connection_flow` | Positive / Network E2E | Enters a valid Home Assistant demo endpoint (`https://demo.home-assistant.io`) and verifies screen transition to connection handshake state. | **PASSED** |

## Author

**Yaroslav Kozakov**
- LinkedIn: [linkedin.com/in/ykozakov](https://www.linkedin.com/in/ykozakov)
- Telegram: [@YKozakov](https://t.me/YKozakov)
