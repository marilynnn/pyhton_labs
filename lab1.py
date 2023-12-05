# 1.Напишите функцию lensort, которая принимает список строк и сортирует его в порядке возрастания их длины.
# Возвращает отсортированный таким образом список. Исходный список должен остаться неизменным.

def lensort (string_list):
    #string_list.sort(key = lambda a: len(a))
    return sorted(string_list, key = len)

string = ["a","kdkdk","dkkd"]
print(string)
sorted_list = lensort(string)
print(sorted_list)


# 1. Используется передача параметров через присваивание.

# 2. Самое простое различие между sort() и sorted(): sort() изменяет список напрямую и не возвращает никакого значения,
# а sorted() не изменяет список и возвращает отсортированный список.
# sort применим только к list, sorted к итерабельным объектам

# 3. Использование lambda с sort:
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# pairs


# 2.Напишите функцию unique, которая удаляет дубликаты из списка и возвращает результат.

def unique(list):
    return set(list)
print(unique([1,2,3,1,2,3]))

# 1.set - множество неповторяющихся объектов.


# 3. Напишите функцию my_enumerate, которая принимает произвольный список,
# и возвращает список кортежей, в каждом из которых два элемента: элемент списка и порядковый номер данного элемента

def my_enumerate(_list):
    return list(zip(range(len(_list)), _list))

print(my_enumerate(["dasha","dzera","ira"]))

# 4. Напишите функцию, принимающую имя файла с текстом
# и подсчитывающую частоту встречающихся в нём слов.
# Каждая линия вывода имеет формат: «<Слово>: <Сколько раз встречается это слово>»
import re
def words_num (file_name):
    with open(file_name, 'r') as file:
        rd = file.read()
        delimeters = "[ \W]+"
        words = dict.fromkeys(re.split(delimeters, rd))
        if '' in words:
            words.pop('')
        for word in words:
            words[word] = rd.count(word)
            print (word, ' : ', words[word])
words_num('input.txt')


#5.	Напишите декоратор, который измеряет время выполнения функции и выводит его в консоль.
# Проверьте его действие на трёх функциях, принимающих список целых чисел и возвращающих список их квадратов, но выполняющих эту задачу тремя способами:
# через цикл for, через list comprehension и с использованием встроенной функции map.

import time
import functools

def time_dec (func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time1 = time.perf_counter()
        res = func(*args, **kwargs)
        time2 = time.perf_counter()
        print(format((time2 - time1), '.9f'))
        return res
    return wrapper

@time_dec
def quad_1(nums):
    quads = []
    for num in nums:
        quads.append(num*num)
    return quads

@time_dec
def quad_2(nums):
   quads = [num*num for num in nums]
   return quads

@time_dec
def quad_3(nums):
    return map(lambda x: x*x, nums)


nums = [1, 2, 3, 4, 5, 6]

print('Loop:')
quad_1(nums)
print('List comprehension:')
quad_2(nums)
print('Map:')
quad_3(nums)

