#Задание "Раз, два, три, четыре, пять .... Это не всё?"
#1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#Выходные данные (консоль): 99

data_structure = [
[1, 2, 3], #list
{'a': 4, 'b': 5}, #dict
(6, {'cube': 7, 'drum': 8}), #tuple
"Hello", #str
((), [{(2, 'Urban', ('Urban2', 35))}]) #tuple,
]

# 1-й вариант решения: здесь помимо функции определяется переменная для суммы вне функции

total_sum = 0
def calculate_structure_sum_1(data):
    global total_sum
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for item in data:
            calculate_structure_sum_1(item)
    elif isinstance(data, dict):
        for value in data.values():
            calculate_structure_sum_1(value)
        for key in data.keys():
            calculate_structure_sum_1(key)
    elif isinstance(data, int):
        total_sum += data
    elif isinstance(data, str):
        total_sum += len(data)
    return total_sum

result_1 = calculate_structure_sum_1(data_structure)
print('Результат 1-го способа решения:', result_1)

# 2-й вариант решения: переменная определяется внутри функции, для рекурсивного подсчета определяется еще одна функция

def calculate_structure_sum_2(data):
    total_sum_2 = 0
    def recurse(data):
        nonlocal total_sum_2
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for item in data:
                recurse(item)
        elif isinstance(data, dict):
            for value in data.values():
                recurse(value)
            for key in data.keys():
                recurse(key)
        elif isinstance(data, int):
            total_sum_2 += data
        elif isinstance(data, str):
             total_sum_2 += len(data)
    recurse(data)
    return total_sum_2

result_2 = calculate_structure_sum_2(data_structure)
print('Результат 2-го способа решения:',result_2)


