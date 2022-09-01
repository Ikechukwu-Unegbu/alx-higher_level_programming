#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdirectory = a_dictionary.copy()
    list_keys = list(newdirectory.keys())

    for i in list_keys:
        newdirectory[i] *= 2

    return (newdirectory)
