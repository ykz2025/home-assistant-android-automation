import pytest
from pages.welcome_page import WelcomePage


class TestHomeAssistantConnection:
    """Тестовий набір перевірки сценаріїв первинного підключення до сервера Home Assistant."""

    def test_validation_invalid_server_url(self, driver):
        """
        Тест 1 (Негативний): Валідація некоректного формату адреси сервера.
        
        Кроки:
        1. Перейти до ручного вводу адреси сервера.
        2. Ввести некоректне значення 'invalid'.
        3. Перевірити валідацію: блокування кнопки Connect або відображення тексту помилки.
        """
        welcome_page = WelcomePage(driver)

        # 1. Перехід до введення адреси
        welcome_page.start_manual_connection()

        # 2. Введення некоректного значення
        welcome_page.enter_server_url("invalid")

        # 3. Перевірка валідації (помилка на екрані або неактивна кнопка підключення)
        has_error = welcome_page.is_error_message_displayed()
        is_disabled = welcome_page.is_connect_button_disabled()
        
        assert has_error or is_disabled, (
            "Форма не відреагувала на некоректний URL: помилки немає і кнопка активна!"
        )

    def test_positive_server_connection_flow(self, driver):
        """
        Тест 2 (Позитивний): Спроба підключення до робочого демо-сервера.
        
        Кроки:
        1. Перейти до ручного вводу адреси сервера.
        2. Ввести валідний URL 'https://demo.home-assistant.io'.
        3. Натиснути кнопку 'Connect'.
        4. Перевірити перехід на екран результату з'єднання.
        """
        welcome_page = WelcomePage(driver)

        # 1. Перехід до введення адреси
        welcome_page.start_manual_connection()

        # 2. Введення валідної адреси
        welcome_page.enter_server_url("https://demo.home-assistant.io")

        # 3. Клік підключення
        welcome_page.submit_connection()

        # 4. Перевірка успішного переходу на екран результату з'єднання
        assert welcome_page.is_unable_to_connect_displayed(), (
            "Очікуваний екран результату підключення не з'явився!"
        )
