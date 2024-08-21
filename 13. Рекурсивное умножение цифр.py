def get_multiplied_digits(number):
    # Преобразуем число в строку, чтобы получить доступ к его цифрам
    str_number = str(number)

    # Если длина строки больше 1, отделяем первую цифру
    if len(str_number) > 1:
        first = int(str_number[0])  # первая цифра в числовом представлении
        return first * get_multiplied_digits(int(str_number[1:]))  # рекурсивный вызов с оставшимися цифрами
    else:
        # Если длина строки не больше 1, то возвращаем единственную цифру
        return int(str_number)  # возвращаем оставшуюся цифру как целое число


# Пример использования функции
result = get_multiplied_digits(40203)
print(result)  # Ожидаемый вывод: 24