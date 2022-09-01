#!/usr/bin/python3
def subtract(list_of_numbers):
    sub = 0
    maximumlist = max(list_of_numbers)

    for n in list_of_numbers:
        if maximumlist > n:
            sub += n

    return (maximumlist - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_roman = 0
    list_of_numbers = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_roman:
                    num += subtract(list_of_numbers)
                    list_of_numbers = [rom_n.get(ch)]
                else:
                    list_of_numbers.append(rom_n.get(ch))

                last_roman = rom_n.get(ch)

    num += subtract(list_of_numbers)

    return (num)
