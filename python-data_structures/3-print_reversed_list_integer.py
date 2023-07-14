#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list = []
    if isinstance(my_list, list):
        for num in reversed(my_list):
            print(num).format(num)
