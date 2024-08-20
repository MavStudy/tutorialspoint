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
    Updating Map

    When the element of the dictionary is updated, the result is instantly
    updated in the result of the ChainMap. In the below example we see that
    the new updated value reflects in the result without explicitly applying
    the ChainMap method again.

    :return:
    """
    separator()

    dict1 = {'day1': 'Mon', 'day2': 'Tue'}
    dict2 = {'day3': 'Wed', 'day4': 'Thu'}

    res = co.ChainMap(dict1, dict2)

    # Creating a single dictionary
    print(f"res: {type(res)}")
    print(res.maps, '\n')

    dict2['day4'] = 'Fri'
    print(res.maps, '\n')


if __name__ == '__main__':
    main()
