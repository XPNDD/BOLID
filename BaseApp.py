from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создание базового класса и методов для работы с WebDriver
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://online.bolid.ru:5000/login'

    def find_element(self, locator, time=2):  # Поиск 1 элемента по локатору
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Не удалось найти элемент {locator}')

    def find_elements(self, locator, time=2):  # Поиск всех элементов по локатору
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Не удалось найти элементы {locator}')

    def go_to_page(self):  # Переход на страницу по url
        return self.driver.get(self.base_url)



