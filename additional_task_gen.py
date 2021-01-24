# Task: написать свой генератор для считывания файлов один раз
import os


def my_gen():
    for file in os.listdir(r'G:\Users\Камиль\Downloads'):
        yield file


x = my_gen()
print([file for file in x])
print([file for file in x])
