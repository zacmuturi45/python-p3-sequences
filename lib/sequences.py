#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        x = 2
        my_list = [0, 1]
        while x < length:
            my_list.append(my_list[x-1] + my_list[x-2])
            x += 1
        print(my_list)





