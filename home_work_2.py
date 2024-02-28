# 1. Створити змінні таких типів:
# string, integer, float, bool, list, dict, tuple, None

string = 'hello'
print(string)

integer_number = 10
print(integer_number)

float_number = 1.5
print(float_number)

bool_1 = True
print(bool_1)

bool_2 = False
print(bool_2)

test_list = [1, 2.5, 'hello', [4, 5]]
print(test_list)

test_dict = {'name': 'Kate', 'city': 'Kyiv', 'country': 'Ukraine'}
print(test_dict)

test_tuple = (1, 2.5, 'hello', (4, 5))
print(test_tuple)

something = None
print(something)


# 2. Використати вивчені оператори та порівняти між собою
# числа, рядки, булеві значення, списки, словники і кортежі

add = integer_number + float_number
print(add)

dec = integer_number - float_number
print(dec)

mul = integer_number * float_number
print(mul)

div = integer_number / float_number
print(div)

div_2 = integer_number // float_number
print(div_2)

mod = integer_number % float_number
print(mod)

power = integer_number ** 2
print(power)

eq = integer_number == float_number
print(eq)

not_eq = integer_number != float_number
print(not_eq)

inc = integer_number > float_number
print(inc)

dig = integer_number < float_number
print(dig)

result_1 = integer_number < 50 and string == 'hello'
print(result_1)

result_2 = float_number > 20 or string not in test_list
print(result_2)

# Робота з рядками:

# 1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()

num_str = 125
num = str(num_str)
print(num)

#  2. Cтворити зміну message = 'Hi, my name is Python!'
#  За допомогою функції replace() замінити усі букви 'y' на '0' та 'i' на '1'

message = 'Hi, my name is Python!'
message = message.replace('y', '0')
message = message.replace('i', '1')
print(message)

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
# допомогою функції split(), а потім знову обʼєднати у строку
# за допомогою функції join() у змінну string_join

split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)

string_join = " ".join(split_test)
print(string_join)

# 4. Визначити довжину рядку string_join за допомогою функції len()

print(len(string_join))

# Робота зі списками

#  1. Cтворити змінну list_append = [1, 2, 3]. За допомогою функції append() додати туди спочатку 4, а потім 5

list_append = [1, 2, 3]
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9]
#  за допомогою функції extend()

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()

print(list_extend.index(6))

#  4. Визначити довжину списку list_append за допомогою функції len()

print(len(list_append))

# Робота зі словниками

#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
#  та вивести на екран дані, які знаходяться в ключах car та where

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])

#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення

print(dict_test.keys(), dict_test.values())

#  3. За допомогою функції items() вивести на екран пари ключ - значення

print(dict_test.items())
