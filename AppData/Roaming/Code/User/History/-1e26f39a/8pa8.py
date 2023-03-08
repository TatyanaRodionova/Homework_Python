# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

def get_user_number(msg, count):

    count += 1    
    print(f"{msg} №{count}: ")
    user_input = int(input())

    result = (user_input, count)
    return result;

def list_maker(userNumber, msg, count):
    
    result = [random.randint(1, 7) for i in range(userNumber)]
    print(f"{msg}{count}: {result}")
    print()
    
    return result

count_get_user_number = 0
message_for_user_1 = 'Введите количество элементов множества'
message_for_user_2 = 'Множество №'

list_1_elements = get_user_number(msg = message_for_user_1, count = count_get_user_number)
(list_1_lenght, count_get_user_number) = list_1_elements
list_1 = list_maker(userNumber = list_1_lenght, msg = message_for_user_2, count = count_get_user_number)

list_2_elements = get_user_number(msg = message_for_user_1, count = count_get_user_number)
(list_2_lenght, count_get_user_number) = list_2_elements
list_2 = list_maker(userNumber = list_2_lenght, msg = message_for_user_2, count = count_get_user_number)

list_1_set = set(list_1)
list_2_set = set(list_2)

common_set = set(list_1) & set(list_2)
result = sorted(common_set)
print(f"Пересечение множеств №{count_get_user_number - 1} и №{count_get_user_number}, отсортированное по возрастанию: {result}")



# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

import random

def blueberry_field_maker(msg):

    number_of_bushes = random.randint(5, 15)
    bushes = [i for i in range(1, number_of_bushes)]
    bush_crop = [random.randint(1, 10) for i in range(number_of_bushes)]

    result_field = dict(zip(bushes, bush_crop))
    print(f"{msg}{result_field}")

    result = (number_of_bushes, result_field)
    return result

def harvester_position_maker(msg, number):

    result = random.randint(1, number)
    print(f"{msg}{result}")
    return result

def harveter_production_analyze(position, field):

    result = field[position] + field[position + 1] + field[position - 1]
    return result

message_for_user_1 = 'Анализируемое поле: '
message_for_user_2 = 'Позиция комбайна - куст №'
field_elements = blueberry_field_maker(msg = message_for_user_1)
(number_of_bushes, result_field) = field_elements
blueberry_field = result_field
harvester_position = harvester_position_maker(msg = message_for_user_2, number = number_of_bushes)

result = harveter_production_analyze(position = harvester_position, field = blueberry_field)
print(f"Объем ягод, который сможет собрать комбайн: {result}")
