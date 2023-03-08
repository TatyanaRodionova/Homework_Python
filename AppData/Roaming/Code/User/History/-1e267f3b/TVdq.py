# Задача 1:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def production(number, power):
    
    if power == 1:
        return number
    else:
        return (number * production(number, power - 1))

print()
powered_number = int(input('Введите число возводимое в степень: '))
power_for_number = int(input('Введите степень, в которую необходимо возвести число: '))
print()

result = production(number = powered_number, power = power_for_number)
print(f'Число {powered_number} в степени {power_for_number} = {result}')

# Задача 2:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

from User_interface_module import get_user_number

def summary(number_1, number_2):

    if number_2 == 0:
        return number_1
    else:
        return summary(number_1 + 1, number_2 - 1)

count_get_user_number = 0
message_for_user_1 = 'Введите '
message_for_user_2 = '-е число: '

print()
first_user_number_elements = get_user_number(msg_1 = message_for_user_1, msg_2 = message_for_user_2 ,count = count_get_user_number)
(first_user_number, count_get_user_number) = first_user_number_elements
second_user_number_elements = get_user_number(msg_1 = message_for_user_1, msg_2 = message_for_user_2 ,count = count_get_user_number)
(second_user_number, count_get_user_number) = second_user_number_elements
print()

result = summary(number_1 = first_user_number, number_2 = second_user_number)
print(f'Сумма чисел {first_user_number} и {second_user_number} = {result}')

# Класс функций для взаимодействия с пользователем

# Метод проверки правильности ввода (ожидается ввод целого числа)
def get_user_number(msg_1: str, msg_2: str, count: int) -> tuple[int, int]:
    
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