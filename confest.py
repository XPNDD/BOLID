import pytest
from selenium import webdriver


# Создание фикстуры для подготовки начального состояния системы для проведения тестирования

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()  # Указание веб-драйвера
    yield driver
    driver.quit()  # Отключение веб-драйвера после прохождения всех тестов

