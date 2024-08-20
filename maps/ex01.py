# coding=utf-8
"""
Python - Maps

Python Maps also called ChainMap is a type of data structure to manage multiple
dictionaries together as one unit. The combined dictionary contains the key
and value pairs in a specific sequence eliminating any duplicate keys. The best
use of ChainMap is to search through multiple dictionaries at a time and get
the proper key-value pair mapping. We also see that these ChainMaps behave as
stack data structure.

https://www.tutorialspoint.com/python_data_structure/python_maps.htm
"""
import collections as co


def separator(col=30):
    print('-' * col)


def main():
    """
    Creating a ChainMap

    We create two dictionaries and club them using the ChainMap method from the
    collections library. Then we print the keys and values of the result of the
    combination of the dictionaries. If there are duplicate keys, then only the
    value from the first key is preserved.

    :return:
    """
    separator()

    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}

    res = co.ChainMap(dict1, dict2)

    # Creating a single dictionary
    print(f"res: {type(res)}")
    print(res.maps, '\n')

    # print('Keys = {}'.format(list(res.keys())))
    print(f"Keys = {list(res.keys())}")
    # print('Values = {}'.format(list(res.values())))
    print(f"Values = {list(res.values())}")
    print()

    # Print all the elements from the result
    print('elements:')
    for key, val in res.items():
        # print('{} = {}'.format(key, val))
        print(f"{key} = {val}")
    print()

    # Find a specific value in the result
    # print('day3 in res: {}'.format(('day1' in res)))
    print(f"day3 in res: {'day1' in res}")
    # print('day4 in res: {}'.format(('day4' in res)))
    print(f"day4 in res: {'day4' in res}")



if __name__ == '__main__':
    main()
