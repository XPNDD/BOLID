import random
import string
import pytest


# Создание алфавитов для генерации логина и пароля
cyrillic_letters_temp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyrillic_letters = cyrillic_letters_temp.lower() + cyrillic_letters_temp.upper()  # Кириллица
chars = string.ascii_letters + string.digits + ' ' + string.punctuation + cyrillic_letters  # Латинский алфавит,
# цифры и спецсимволы


# Генерация trash-data
def generate_trash() -> list:
    storage = []
    for _ in range(100):
        item_1 = ''.join(random.choice(chars) for _ in range(random.randint(0, 100)))
        item_2 = ''.join(random.choice(chars) for _ in range(random.randint(0, 100)))
        storage.append((item_1, item_2))
    return storage


# Вспомогательная функция для генерации случайных текстовых данных из заданного алфавита и границ возможной длины
def create_item(alphabet: str, min_length, max_length) -> str:
    item = ''.join(random.choice(alphabet) for _ in range(random.randint(min_length, max_length)))
    return item


# "Склеивание" 2ух списков (из сгенерированных логинов и паролей) в 1 с кортежами
def generate_data(usernames, passwords) -> list:
    pairs = []
    iter_count = 0
    for username in usernames:
        for password in passwords:
            iter_count += 1
            pairs.append(pytest.param((username, password), id=str(iter_count)))
    return pairs


# Генерация корректных данных для логина
def generate_correct_login() -> list:
    storage = []
    data_min_len = 1
    data_max_len = 63
    for _ in range(4):
        item_1 = create_item(string.ascii_letters, data_min_len, data_max_len)
        item_2 = int(create_item(string.digits, data_min_len, data_max_len))
        item_3 = create_item(string.ascii_letters + string.digits, data_min_len, data_max_len)
        temp_list = [item_1, item_2, item_3]
        storage.extend(temp_list)
    return storage


# Генерация корректных данных для пароля
def generate_correct_password() -> list:
    storage = []
    data_min_len = 1
    data_max_len = 63
    for _ in range(4):
        item_1 = create_item(string.ascii_letters, data_min_len, data_max_len)
        item_2 = int(create_item(string.digits, data_min_len, data_max_len))
        item_3 = create_item(string.punctuation, data_min_len, data_max_len)
        item_4 = create_item(string.ascii_letters + string.digits, data_min_len, data_max_len)
        item_5 = create_item(string.ascii_letters + string.punctuation, data_min_len, data_max_len)
        item_6 = create_item(string.ascii_letters + string.digits + string.punctuation, data_min_len, data_max_len)
        temp_list = [item_1, item_2, item_3, item_4, item_5, item_6]
        storage.extend(temp_list)
    return storage


# Генерация некорректных данных для логина
def generate_incorrect_login() -> list:
    storage = []
    data_min_len = 1
    data_max_len = 64
    for _ in range(4):
        item_1 = create_item(cyrillic_letters, data_min_len, data_max_len)
        item_2 = create_item(cyrillic_letters + string.ascii_letters, data_min_len, data_max_len)
        item_3 = create_item(cyrillic_letters + string.digits, data_min_len, data_max_len)
        item_4 = create_item(cyrillic_letters + string.punctuation, data_min_len, data_max_len)
        item_5 = create_item(cyrillic_letters + string.ascii_letters + string.digits, data_min_len, data_max_len)
        item_6 = create_item(cyrillic_letters + string.ascii_letters + string.digits + string.whitespace, data_min_len, data_max_len)
        item_7 = create_item(string.punctuation, data_min_len, data_max_len)
        item_8 = create_item(string.whitespace, data_min_len, data_max_len)
        temp_list = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8]
        storage.extend(temp_list)
    # Генерация пароля с корректными символами, но недопустимой длины
    item_9 = create_item(string.ascii_letters, 64, 100)
    item_10 = create_item(string.ascii_letters, 0, 0)
    storage.extend([item_9, item_10])
    return storage


# Генерация некорректных данных для пароля
def generate_incorrect_password() -> list:
    storage = []
    data_min_len = 1
    data_max_len = 64
    for _ in range(4):
        item_1 = create_item(cyrillic_letters, data_min_len, data_max_len)
        item_2 = create_item(cyrillic_letters + string.ascii_letters, data_min_len, data_max_len)
        item_3 = create_item(cyrillic_letters + string.digits, data_min_len, data_max_len)
        item_4 = create_item(cyrillic_letters + string.punctuation, data_min_len, data_max_len)
        item_5 = create_item(cyrillic_letters + string.ascii_letters + string.digits, data_min_len, data_max_len)
        item_6 = create_item(cyrillic_letters + string.ascii_letters + string.digits + string.whitespace, data_min_len,
                             data_max_len)
        item_7 = create_item(string.whitespace, data_min_len, data_max_len)
        temp_list = [item_1, item_2, item_3, item_4, item_5, item_6, item_7]
        storage.extend(temp_list)
    # Генерация пароля с корректными символами, но недопустимой длины
    item_8 = create_item(string.ascii_letters, 64, 100)
    item_9 = create_item(string.ascii_letters, 0, 0)
    storage.extend([item_8, item_9])
    return storage
