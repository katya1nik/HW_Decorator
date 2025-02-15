# Домашнее задание 📃
## Часть 1: Декоратор для валидации пароля

# >[!info]
# >### Краткое содержание
# >В этом задании вы создадите декоратор для проверки сложности пароля и функцию регистрации пользователей. Декоратор будет проверять, соответствует ли пароль заданным критериям безопасности.

### Технологии: 🦾
# - Python
# - Декораторы
# - Аннотации типов

## Задание 👷‍♂️

### Декоратор и его функциональность

# 1. **Декоратор `password_checker`**
# 	- **Функциональность**: Проверяет сложность пароля.
# 	- **Критерии проверки пароля**:
# 	- Минимальная длина: 8 символов.
# 	- Содержит хотя бы одну цифру.
# 	- Содержит хотя бы одну заглавную букву.
# 	- Содержит хотя бы одну строчную букву.
# 	- Содержит хотя бы один специальный символ (например, !, @, #, $ и т.д.).
# 	- **Поведение**: Если пароль соответствует всем условиям, декоратор вызывает оригинальную функцию. В противном случае возвращает сообщение об ошибке.
# 2. **Функция `register_user`**
# 	- **Аргументы**: Принимает пароль в качестве аргумента.
# 	- **Возвращаемое значение**: Сообщение об успешной регистрации, если пароль прошел проверку, или сообщение об ошибке в противном случае.
# 	- **Применение декоратора**: Используйте `@password_checker` для автоматической проверки пароля. 

### Примеры использования

# - Вызовите `register_user` с различными паролями, включая те, которые соответствуют всем условиям, и те, которые не соответствуют хотя бы одному из условий.
# - Выведите соответствующие сообщения об успешной регистрации или об ошибках.

### Таблица функций и декораторов:

# | Элемент                  | Описание                                                    |
# | ------------------------ | ----------------------------------------------------------- |
# | `password_checker`       | Декоратор для проверки сложности пароля.                    |
# | `register_user`          | Функция для регистрации пользователя с проверкой пароля.    |

# >[!warning]
# >### Критерии проверки 👌
# >1. Код должен быть чистым и легко читаемым.
# >2. Имена переменных и функций должны быть осмысленными и понятными.
# >3. Все функции и переменные должны быть аннотированы типами, включая использование модуля `Typing`.
# >4. Программа должна успешно проходить проверку `mypy` для проверки типов.
# >5. Код должен быть протестирован с различными вариантами паролей, чтобы убедиться, что декоратор корректно обрабатывает различные ситуации.

# ---


## Часть 2: Декораторы для валидации данных

# >[!info]
# >### Краткое содержание
# >В этом задании вы создадите два декоратора для проверки пользовательских данных перед их сохранением в CSV файл. Один декоратор будет проверять сложность пароля, а второй — корректность имени пользователя.

### Технологии: 🦾
# - Python
# - Декораторы
# - Работа с файлами CSV
# - Исключения

## Задание 👷‍♂️

### Декораторы и их функциональность

# 1. **Декоратор `password_validator`**
#    - **Параметры**:
#      - `min_length`: Минимальная длина пароля (по умолчанию 8).
#      - `min_uppercase`: Минимальное количество заглавных букв (по умолчанию 1).
#      - `min_lowercase`: Минимальное количество строчных букв (по умолчанию 1).
#      - `min_special_chars`: Минимальное количество специальных символов (по умолчанию 1).
#    - **Функциональность**:
#      - Проверяет, соответствует ли пароль заданным критериям.
#      - Если пароль не соответствует, выбрасывает `ValueError` с описанием проблемы.

# 2. **Декоратор `username_validator`**
#    - **Функциональность**:
#      - Проверяет, что в имени пользователя отсутствуют пробелы.
#      - Если в имени пользователя есть пробелы, выбрасывает `ValueError` с описанием проблемы.

# 3. **Функция `register_user`**
#    - **Аргументы**: Принимает `username` и `password`.
#    - **Функциональность**:
#      - Дозаписывает имя пользователя и пароль в CSV файл.
#      - Оборачивается обоими декораторами для валидации данных.

### Пример использования


# ```python
# import csv

# def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1):
    # """
    # Декоратор для валидации паролей.

    # Параметры:
    #     length (int): Минимальная длина пароля (по умолчанию 8).
    #     uppercase (int): Минимальное количество букв верхнего регистра (по умолчанию 1).
    #     lowercase (int): Минимальное количество букв нижнего регистра (по умолчанию 1).
    #     special_chars (int): Минимальное количество спец-знаков (по умолчанию 1).

    # Пример использования:
    # @password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
    # def register_user(username: str, password: str):
    #     pass
    # """

# def username_validator():
# pass


# @password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
# @username_validator
# def register_user(username: str, password: str):
#     """
    # Функция для регистрации нового пользователя.

    # Параметры:
    #     username (str): Имя пользователя.
    #     password (str): Пароль пользователя.

    # Raises:
    #     ValueError: Если пароль или юзернейм не соответствует заданным условиям.
    
    # Запись имени пользователя и пароля в CSV файл


# Тестирование успешного случая
# try:
#     register_user("JohnDoe", "Password123!")
#     print("Регистрация прошла успешно!")
# except ValueError as e:
#     print(f"Ошибка: {e}")

# Тестирование неудачного случая по паролю...


# Тестирование неудачного случая по юзернейму...

'''

Таблица декораторов и функций:

| Элемент                | Описание                                                                 |
| ---------------------- | ------------------------------------------------------------------------ |
| `password_validator`   | Декоратор для проверки сложности пароля.                                 |
| `username_validator`   | Декоратор для проверки корректности имени пользователя.                  |
| `register_user`        | Функция для регистрации пользователя и сохранения данных в CSV файл.     |

>[!warning]
>### Критерии проверки 👌
>1. Код должен соответствовать стандарту PEP-8.
>2. Все функции и переменные должны быть аннотированы типами.
>3. Должны присутствовать док-стринги для всех функций и декораторов.
>4. Код должен успешно проходить проверку типов с использованием `mypy`. (Опционально)
>5. Все проверки должны быть реализованы и работать корректно.
>6. 3+ коммита на GitHub
'''

from typing import Callable, Any
import csv
def password_checker(func: Callable) -> Callable:
    def wrapper(username: str, password: str) -> str:
        """
        Проверка пароля на длину
        """
        if len(password) < 8:
            return "Пароль должен содержать не менее 8 символов"

        """
        Проверка пароля на наличие цифр
        """
        if not any(char.isdigit() for char in password):
            return "Пароль должен содержать хотя бы одну цифру"

        """
        Проверка пароля на наличие заглавных букв
        """
        if not any(char.isupper() for char in password):
            return "Пароль должен содержать хотя бы одну заглавную букву"

        """
        Проверка пароля на наличие строчных букв
        """
        if not any(char.islower() for char in password):
            return "Пароль должен содержать хотя бы одну строчную букву"
    
        """
        Проверка пароля на наличие специальных символов
        """
        if not any(char in "!@#$%^&*()_+-=[]{}|;':,.<>?/" for char in password):
            return "Пароль должен содержать хотя бы один специальный символ"

        return func(username, password)
    return wrapper

@password_checker
def register_user(username: str, password: str) -> str:
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    return f"Пользователь {username} успешно зарегистрирован, пароль: {password}"

# Примеры использования:
print(register_user("JohnDoe", "weak"))
print(register_user("Alice", "password123"))
print(register_user("Bob", "Password123"))
print(register_user("Charlie", "Password123!"))

def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1,  special_chars: int  = 1):
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> str:
            if len(password) < length:
                raise ValueError(f"Пароль должен содержать не менее {length} символов")

            upper_count = sum(1 for char in password if char.isupper())
            if upper_count < uppercase:
                raise ValueError(f"Пароль должен содержать  минимум {uppercase} заглавную букву")

            lower_count = sum(1 for char in password if char.islower())
            if lower_count < lowercase:
                raise ValueError(f"Пароль должен содержать не менее {lowercase} строчной буквы")

            sh = "!@#$%^&*()_+-=[]{}|;':,.<>?/"
            special_count = len([char for char in password if char in sh])
            if special_count < special_chars:
                raise ValueError(f"Пароль должен содержать не менее {special_chars} специальных символов")

            return func(username, password)
        return wrapper
    return decorator

def username_validator():
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> str:
            if ' ' in username:
                raise ValueError("Имя пользователя не должно содержать пробелы")
            return func(username, password)
        return wrapper
    return decorator
 
    
@password_validator(length=8, uppercase=1, lowercase=1, special_chars=1)
@username_validator()
def register_user(username: str, password: str) -> str:
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    return(f"Пользователь {username} успешно зарегистрирован")

# Проверка:
try:
    register_user("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print(register_user("John Doe", "Password123!"))  # ошибка пробела в имени
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print(register_user("Alice", "Weakweak"))  # ошибка слабого пароля
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print(register_user("Bob", "Password1"))  # Нет спецсимволов
except ValueError as e:
    print(f"Ошибка: {e}")