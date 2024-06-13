def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) <= 1:
        return int(str_number)
    else:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))

number = 1234
result = get_multiplied_digits(number)
print(f"Произведение цифр числа {number} равно: {result}")