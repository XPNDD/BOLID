from BaseApp import BasePage
from selenium.webdriver.common.by import By


# Запись локаторов для каждого из используемых объектов на веб-странице
class PageLocators:
    LOGIN_FIELD_LOCATION = (By.ID, 'email')
    PASSWORD_FIELD_LOCATION = (By.ID, 'password')
    SIGN_IN_BUTTON_LOCATION = (By.XPATH, '/html/body/div[1]/main/div/div/div/div/form/button')
    ALERT_LOCATION = (By.CLASS_NAME, 'toast-message-detail')


# Создание класса с вспомогательными методами
class InputHelper(BasePage):
    def enter_login(self, login):  # Ввод логина в соответствующее поле
        login_field = self.find_element(PageLocators.LOGIN_FIELD_LOCATION)
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):  # Ввод пароля в соответствующее поле
        password_field = self.find_element(PageLocators.PASSWORD_FIELD_LOCATION)
        password_field.send_keys(password)
        return password_field

    def button_is_enabled(self):  # Проверка кнопки на возможность взаимодействия
        return self.find_element(PageLocators.SIGN_IN_BUTTON_LOCATION, time=1).is_enabled()

    def click_sign_in_button(self):  # Нажатие на кнопку
        return self.find_element(PageLocators.SIGN_IN_BUTTON_LOCATION, time=1).click()

    def get_alert_text(self):  # Получение текста предупреждения
        return self.find_element(PageLocators.ALERT_LOCATION, time=1).text

