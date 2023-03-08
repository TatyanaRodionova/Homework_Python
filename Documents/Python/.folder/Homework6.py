# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод:
# 7 2 5
# Вывод:
# 7 9 11 13 15


from User_interface_module import get_user_data

def progression_maker(number_1, number_2, number_3):
    
    list_maker(number_1, number_3)

    if number_3 == 1:
        return number_1
    else:
        return progression_maker(number_1 + number_2, number_2, number_3 - 1)

# 1 + 2 = **3**, 2 ,4
#     3 + 2 = **5**, 2, 3
#         5 + 2 = **7**, 2, 2
#             7 + 2 = **9**, 2, 1
#                         **1**

# Аргумент по умолчанию создаётся один раз.
# Поэтому, если в качестве аргумента по умолчанию выбрать изменяемый тип данных (словарь или список),
# то он будет общим у всех вызовов функции.
# Соответственно, если вы один раз вызовете функцию с аргументом по умолчанию и внутри неё в этот аргумент добавите элементы,
# то они будут там и при следующем вызове этой функции.

# Почему тип данных для result, получаемого как:
# result = some_list.append(next_element)
# None?
# Методы, которые добавляют, вычитают или переставляют элементы на месте и не возвращают конкретный элемент,
# никогда не возвращают сам экземпляр коллекции, а None.

def list_maker(next_element, final_signal, some_list = []):
    
    some_list.append(next_element)
    result = some_list

    if final_signal == 1:
        print (f'Получена последовательность: {str(result)[1:-1]}')

message_for_user_1 = 'Введите первый элемент последовательности: '
message_for_user_2 = 'Введите шаг (разность прогрессии) последовательности: '
message_for_user_3 = 'Введите количество элементов последовательности: '

user_data = get_user_data(msg_1 = message_for_user_1, \
                               msg_2 = message_for_user_2, \
                               msg_3 = message_for_user_3)

(progression_first_element, progression_step, progression_length) = user_data

progression_maker(number_1 = progression_first_element, \
                  number_2 = progression_step, \
                  number_3 = progression_length)
# Класс функций для взаимодействия с пользователем

# Метод проверки правильности ввода (ожидается ввод целого числа)
def get_user_data_check(msg_1: str, msg_2: str, count: int) -> tuple[int, int]:
    
    count += 1

    print(f"{msg_1}{count}{msg_2}", end = '')
    
    while(True):
        try:
            user_input = int(input())
            if (type(user_input) == int):
                result = (user_input, count)
                return(result)
            else:
                raise ValueError
        except ValueError:
            print("Введенное значение не соответствует условиям задачи, повторите ввод.")

# Метод получения данных от пользователя с выводом запроса(-ов) в виде текста
def get_user_data(msg_1: str, msg_2: str, msg_3: str) -> tuple[int, int, int]:
    
    print()
    user_data_1 = int(input(msg_1))
    user_data_2 = int(input(msg_2))
    user_data_3 = int(input(msg_3))
    print()

    result = (user_data_1, user_data_2, user_data_3)
    return result

    # Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:
# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод:
# [1, 9, 13, 14, 19]

from Random_collections_maker_module import list_maker
from User_interface_module import get_user_data

def array_check(array, search_range):

    indexes_list = []
    min_border = search_range[0]
    max_border = search_range[1]

    for element_index in range(len(array)):
        if (array[element_index] >= min_border and array[element_index] <= max_border):
            indexes_list.append(element_index)
    
    result = indexes_list
    return result

message_for_user_1 = 'Укажите длину массива: '
message_for_user_2 = 'Укажите минимально возможное значение элемента массива: '
message_for_user_3 = 'Укажите максимально возможное значение элемента массива: '
message_for_user_4 = 'Укажите нижнюю границу поиска элементов массива: '
message_for_user_5 = 'Укажите верхнюю границу поиска элементов массива: '

list_of_messages = message_for_user_1, message_for_user_2, message_for_user_3
array_parameters = get_user_data(messages = list_of_messages)

(checking_arr_length, checking_arr_min, checking_arr_max) = array_parameters

checking_array = list_maker(arr_length = checking_arr_length,\
                          arr_min = checking_arr_min,\
                          arr_max = checking_arr_max)

print()
print(f'Получен массив: {str(checking_array)[1:-1]}')

list_of_messages = message_for_user_4, message_for_user_5
checking_array_search_range = get_user_data(messages = list_of_messages)

print()
print(f'Диапазон поиска: {checking_array_search_range}')

result = array_check(array = checking_array, search_range = checking_array_search_range)
print()
print(f'Индексы элементов массива, значения которых принадлежат заданному диапазону: {result}')
# Класс функций для создания рандомных колеекций

# Метод генерации заданной длины массива целых чисел заданном диапазоне
# (ожидается ввод длины массива и границ диапазона)
import random

def list_maker(arr_length: int, arr_min: int, arr_max: int) -> list[int]:
    
    result = [random.randint(arr_min, arr_max) for i in range(arr_length)]
    
    return result

# Класс функций для взаимодействия с пользователем

# Метод проверки правильности ввода (ожидается ввод целого числа)
def get_user_data_check(msg_1: str, msg_2: str, count: int) -> tuple[int, int]:
    
    count += 1

    print(f"{msg_1}{count}{msg_2}", end = '')
    
    while(True):
        try:
            user_input = int(input())
            if (type(user_input) == int):
                result = (user_input, count)
                return(result)
            else:
                raise ValueError
        except ValueError:
            print("Введенное значение не соответствует условиям задачи, повторите ввод.")

# Метод получения данных от пользователя с выводом запроса(-ов) в виде текста
def get_user_data(messages: tuple[str]) -> tuple[int]:
    
    user_data_list = []

    number_of_messages = len(messages)

    for i in range(number_of_messages):
        print()
        user_data = int(input(messages[i]))
        user_data_list.append(user_data)
    
    result = user_data_list
    return result

    