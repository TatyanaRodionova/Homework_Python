# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0

from random import randint # Импортируем функцию randint из модуля random

m = int(input('Введите число монеток: '))
print()

rawOfCoins = [] # Объявляем список "rawOfCoins" 

# Заполняем "rawOfCoins" подкидыванием монеток
for i in range(m):
    coin = randint(0, 1) # Подкидываем монетку
    rawOfCoins.insert(i, coin) # Добавляем подкинутую монетку в "rawOfCoins"

n0 = rawOfCoins.count(0) # Считаем количество монет со значением "0"
n1 = rawOfCoins.count(1) # Считаем количество монет со значением "1"

print(f'Для полученных {m} монет выпали следующие значения: {rawOfCoins}.'
    f'В том числе значения \"0\" для {n0} монет, '
    f'значения \"1\" для {n1} монет.') # Выводим выпавшие значения монеток из "rawOfCoins"

# Проверяем каких монет больше и выводим наименьшее значение.
if (n0 >= n1): print(f'Необходимо перевернуть {n1} монет.')
else: print(f'Необходимо перевернуть {n0} монет.')

# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2


from random import randint # Импортируем функцию randint из модуля random

firstNumber = randint(0, 1001) # Придумываем первое число
secondNumber = randint(0, 1001)# Придумываем второе число

sumOfNumbers = firstNumber + secondNumber
productOfNumbers = firstNumber * secondNumber

# Выводим подсказку
print(f'Загадано два числа.\nСумма этих чисел = {sumOfNumbers}.'
    f'\nпроизведение этих чисел = {productOfNumbers}.\n')

# Делаем квадратное уравнение из системы двух уравнений
# sumOfNumbers = firstNumber + secondNumber
# productOfNumbers  =  firstNumber * secondNumber
# productOfNumbers = (sumOfNumbers - secondNumber) * secondNumber
# productOfNumbers = sumOfNumbers * secondNumber - secondNumber ** 2
# secondNumber ** 2 - sumOfNumbers * secondNumber + productOfNumbers

# Уравнение приведенное (старший коэффициент == 1) => искомые числа являются корнями этого уравнения

d = sumOfNumbers ** 2 - 4 * productOfNumbers # Ищем дискрименант

secondNumber = int(sumOfNumbers / 2 + d ** (0.5) / 2)
firstNumber = int(sumOfNumbers / 2 - d ** (0.5) / 2)

print(f'Загаданные числа это: {firstNumber} и {secondNumber}.')

# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8
