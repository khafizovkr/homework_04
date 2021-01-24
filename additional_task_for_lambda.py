# Task попробовать заменить на лямбда функцию my_f
from functools import reduce

random_str = ['a', 'b', 'c', 'b', 'd']
my_f = lambda symbol_1, symbol_2: symbol_1 + symbol_2
print(reduce(my_f, random_str))
