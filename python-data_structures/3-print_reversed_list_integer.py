#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list=[0, 1, 2]
    if isinstance(my_list, list):
        my_list.reverse()
    for num in my_list:
        print('{:d}'.format(num))
