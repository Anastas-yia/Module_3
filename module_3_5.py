#Задача "Рекурсивное умножение цифр"

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    while str_number.endswith('0'):  # отсекаем нули в конце number
        str_number = str_number[:len(str_number) - 1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203) #пример результата выполнения программы из задания
print(result)
# если не убирать 0 в конце числа, то результат всегда будет 0
result_1 = get_multiplied_digits(402030000)
print(result_1)

result_2 = get_multiplied_digits(10)
print(result_2)
