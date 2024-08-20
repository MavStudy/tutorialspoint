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
    Map Reordering

    If we change the order the dictionaries while clubbing them in the above
    example we see that the position of the elements get interchanged as if
    they are in a continuous chain. This again shows the behavior of Maps
    as stacks.


    :return:
    """
    separator()

    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day1': 'Thu'}

    res1 = co.ChainMap(dict1, dict2)

    # Creating a single dictionary
    print(f"res1: {type(res1)}")
    print(res1.maps, '\n')

    print()

    res2 = co.ChainMap(dict2, dict1)
    print(res2.maps, '\n')


if __name__ == '__main__':
    main()
