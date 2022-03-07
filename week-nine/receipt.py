"""Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
Prints the products_dict.
Opens the request.csv file for reading.
Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop, your program must do the following for each row:
Use the requested product number to find the corresponding item in the products_dict.
Print the product name, requested quantity, and product price.
"""

import csv
from itertools import product
from statistics import quantiles
from urllib import request
PRODUCT = 0
NAME = 1
PRICE = 2
QUANTITY= 1  


def main(): 
    product_dictionary = read_dict("products.csv", PRODUCT)
    for product_key, product_list in product_dictionary.items(): 
        name = product_list[NAME]
        price = product_list[PRICE]
        print(f"{product_key} {product_list}")
    print("")
    print("Reqested Items")

    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)
        for row_list in reader:
            id = row_list[PRODUCT]
            if id in product_dictionary:
                product_list = product_dictionary[id]
                name = product_list[NAME]
                quantity = row_list[1]
                price = product_list[PRICE]
                print(f"{name}: {quantity} at {price}")
        




def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.s

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dict = {}
    with open(filename, 'rt') as shopping_file:
        reader = csv.reader(shopping_file)
        next(reader)
        for row_list in reader:
       
            key = row_list[key_column_index]

            dict[key] = row_list

    return dict
   


if __name__ == "__main__":
    main()