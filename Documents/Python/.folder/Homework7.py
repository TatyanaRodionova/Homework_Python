# Задача 34: 
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

def poem_vowels_count(testing_poem: list, checking_alfabet: set()) -> tuple[int]:

    list_of_vowels_number = []

    for i in range(len(testing_poem)):
        frase_vowels_number = int()
        for j in range(len(checking_alfabet)):
            frase = testing_poem[i]
            count = sum(map(lambda frase: 1 if checking_alfabet[j] in frase else 0, frase))
            frase_vowels_number += count
        list_of_vowels_number.append(frase_vowels_number)

    result = list_of_vowels_number
    return result

message_for_user_1 = 'Введите стихотворение: '
message_for_user_2 = 'Парам пам-пам'
message_for_user_3 = 'Пам парам'
alfabet_vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]

poem = input(message_for_user_1).split(' ')
result = poem_vowels_count(testing_poem = poem, checking_alfabet = alfabet_vowels)

# Если проверять только "а", то можно так:
# poem = list(map(lambda poem: poem.count('а'), poem))

if sum(result) / len(result) == result[0]:
    print(message_for_user_2)
else:
    print(message_for_user_3)

    # Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
 

# def print_operation_table(operation: function, num_rows: int = 6, num_columns: int = 6):
# -> tuple[tuple]


from User_interface_module import get_user_data

def index_maker(parameters: tuple) -> tuple[tuple]:
    
    (strings_number, columns_number) = parameters

    indexes_list = []

    for i in range(1, strings_number + 1):
        for j in range(1, columns_number + 1):
            index = (i, j)
            indexes_list.append(index)
    
    result = indexes_list
    return result

def print_operation_table(indexes: list, parameters: tuple, f) -> tuple[int]:
    
    elements_list = []
    (strings_number, columns_number) = parameters

    for element in indexes:
        element = f(element[0], element[1])
        elements_list.append(element)
    
    result = elements_list

    for i in range(strings_number):
        lower_border = columns_number * i
        upper_border = columns_number * i + columns_number
        i += 1
        print()
        for j in range(lower_border, upper_border):
                print(f"{elements_list[j]:^4}", end = "")
    
    return result

message_for_user_1 = 'Укажите количество строк матрицы: '
message_for_user_2 = 'Укажите количество столбцов матрицы: '

list_of_messages = message_for_user_1, message_for_user_2
user_parameters = get_user_data(messages = list_of_messages)

indexes_list = index_maker(parameters=user_parameters)
element_calculate = lambda x, y: x * y
array2d_elements = print_operation_table(indexes=indexes_list, parameters=user_parameters, f=element_calculate)

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