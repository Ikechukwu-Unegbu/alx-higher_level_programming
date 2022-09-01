#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_of_list = list(a_dictionary.keys())
    order_of_list.sort()
    for i in order_of_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
