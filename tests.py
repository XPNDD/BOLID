import pytest
import requests
from page import InputHelper
from confest import browser
from data_generation import (generate_correct_login, generate_correct_password, generate_incorrect_login,
                             generate_incorrect_password, generate_data, generate_trash)


# Тест работы страницы через код состояния
def test_page_available(browser):
    base_url = InputHelper(browser).base_url
    response_code = requests.get(url=base_url).status_code
    assert response_code == 200


# Тесты с корректными значениями логина и пароля
@pytest.mark.parametrize('credentials', generate_data(generate_correct_login(), generate_correct_password()))
def test_correct_data(credentials: tuple, browser):
    base_page = InputHelper(browser)
    base_page.go_to_page()
    login, password = credentials
    base_page.enter_login(login)
    base_page.enter_password(password)
    if base_page.button_is_enabled():
        base_page.click_sign_in_button()
        # Какое-то действие при входе в систему, например проверка сообщения об удачной авторизации
        assert True
    else:
        assert False


# Тесты с некорректным логином и корректным паролем
@pytest.mark.parametrize('credentials', generate_data(generate_incorrect_login(), generate_correct_password()))
def test_incorrect_login_correct_password(credentials: tuple, browser):
    base_page = InputHelper(browser)
    base_page.go_to_page()
    login, password = credentials
    base_page.enter_login(login)
    base_page.enter_password(password)
    if base_page.button_is_enabled():
        base_page.click_sign_in_button()
        assert base_page.get_alert_text() == 'Неправильно указан логин или пароль.'
    else:
        assert True


# Тесты с корректным логином и некорректным паролем
@pytest.mark.parametrize('credentials', generate_data(generate_correct_login(), generate_incorrect_password()))
def test_correct_login_incorrect_password(credentials: tuple, browser):
    base_page = InputHelper(browser)
    base_page.go_to_page()
    login, password = credentials
    base_page.enter_login(login)
    base_page.enter_password(password)
    if base_page.button_is_enabled():
        base_page.click_sign_in_button()
        assert base_page.get_alert_text() == 'Неправильно указан логин или пароль.'
    else:
        assert True


# Тесты с некорректными логином и паролем
@pytest.mark.parametrize('credentials', generate_data(generate_incorrect_login(), generate_incorrect_password()))
def test_incorrect_data(credentials: tuple, browser):
    base_page = InputHelper(browser)
    base_page.go_to_page()
    login, password = credentials
    base_page.enter_login(login)
    base_page.enter_password(password)
    if base_page.button_is_enabled():
        base_page.click_sign_in_button()
        assert base_page.get_alert_text() == 'Неправильно указан логин или пароль.'
    else:
        assert True


# Тесты с прогоном trash-данных
@pytest.mark.parametrize('credentials', generate_trash())
def test_trash_data(credentials, browser):
    base_page = InputHelper(browser)
    base_page.go_to_page()
    login, password = credentials
    base_page.enter_login(login)
    base_page.enter_password(password)
    if base_page.button_is_enabled():
        base_page.click_sign_in_button()
        assert base_page.get_alert_text() == 'Неправильно указан логин или пароль.'
    else:
        assert True
