#Задача "Распаковка"
#1.Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()              #Вызовите функцию print_params без аргументов
print_params(2)              #Вызовите функцию print_params с разным количеством аргументов
print_params(2, 5)          #Вызовите функцию print_params с разным количеством аргументов
print_params(2, 'замена')       #Вызовите функцию print_params с разным количеством аргументов
print_params(2, 'замена', False)       #Вызовите функцию print_params с разным количеством аргументов
print_params(a = 25, c = 'замена')          #Вызовите функцию print_params с разным количеством аргументов
print_params(b = 25)            #Проверьте, работает ли вызов print_params(b = 25)
print_params(c = [1,2,3])           #Проверьте, работает ли вызов print_params(c = [1,2,3])
print()

#2.Распаковка параметров:
values_list = [11, 'диагональ', (1,2,3)]
values_dict = {'a' : 5, 'b' : 'столбец', 'c' : False}
print_params(*values_list)      #Передала values_list в функцию print_params, используя распаковку параметров
print_params(**values_dict)      #Передала values_dict в функцию print_params, используя распаковку параметров
print()

#3.Распаковка + отдельные параметры:
values_list_2 = [0.125, 'слово']
print_params(*values_list_2, 42)