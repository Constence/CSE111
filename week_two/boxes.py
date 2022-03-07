
import math
"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""

user_items = int(input(f"Enter the number of items: "))
user_num= int(input(f"Enter the number of items per box: "))

#math.celi just rounds to the next whole num 
boxes_math = math.ceil(user_items / user_num)

print()

print(f"For {user_items} items, packing {user_num} items in each box, you will need {boxes_math} boxes.")