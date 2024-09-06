# coding=utf-8
"""
Python-Hash Table

Hash tables are a type of data structure in which the address or the index
value of the data element is generated from a hash function. That makes
accessing the data faster as the index value behaves as a key for the data
value. In other words Hash table stores key-value pairs but the key is
generated through a hashing function.

So the search and insertion function of a data element becomes much faster as
the key values themselves become the index of the array which stores the data.

In Python, the Dictionary data types represent the implementation of hash
tables. The Keys in the dictionary satisfy the following requirements.

• The keys of the dictionary are hashable i.e. the are generated by hashing
  function which generates unique result for each unique value supplied to
  the hash function.

• The order of data elements in a dictionary is not fixed.

So we see the implementation of hash table by using the dictionary data types
as below.

https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm

"""


def main():

    """
    Accessing Values in Dictionary

    To access dictionary elements, you can use the familiar square brackets
    along with the key to obtain its value.

    :return:
    """
    # Declare a dictionary
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    # Accessing the dictionary with its key
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])


if __name__ == '__main__':
    main()
"""
Output: 

dict['Name']:  Zara
dict['Age']:  7
"""
