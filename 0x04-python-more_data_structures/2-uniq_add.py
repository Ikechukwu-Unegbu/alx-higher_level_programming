#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniquelist = set(my_list)
    num = 0

    for i in uniquelist:
        num += i

    return (num)
