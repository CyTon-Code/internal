"""
    Этот модуль сравнивает тип файла с указанным.
    True - Определенно тип совпадает.
    False - Тип не совпал. Одна из букв сравнивая тип с ссылкой не совпала.
    None - Плохое событие. Количество букв в типе больше чем в самой ссылке файла.
или файл в черном списке.
"""


def equal_type(link: str, typ: str) -> bool or None:  # Нужного ли типа файл?  - встроенный модуль
    link = link.lower()  # .png equal .PNG
    typ = typ.lower()  # .png equal .PNG
    n = len(typ)  # -n - это нулевой элемент массива.

    if n > len(link) or typ in ("", "."):
        return None  # тип файла содержит больше букв, чем имя файла или
        # указанный тип есть в черном списке.

    i = 1  # последний элемент масив это: n-1 или -1

    while i <= n:  # Читаю строку типа и сравниваю с строкой.
        if link[-i] != typ[-i]:  # Если нашел не схожие буквы в типе:
            return False

        i += 1

    return True