# 1. Установка зависимостей
### Выполнить команду в терминале:
```
pip install -r requirements.txt
```
### Установить нужный веб-драйвер (geckodriver для FireFox)
# 2. Запуск тестов
### Вариант №1:
Открыть файл test.py и запустить его с помощью кнопки ![Image alt](https://github.com/XPNDD/BOLID/blob/master/md/img.png)
### Вариант №2:
В терминале проекта ввести команду:
```
pytest tests.py
```
Или команду:
```
pytest -v tests.py
``` 
Для более подробного вывода о прохождении тестов
### Вариант №3:
Для запуска 1 конкретного теста ввести команду:
```
pytest tests.py::test_name
``` 
Где ```test_name``` - имя тестовой функции в файле
