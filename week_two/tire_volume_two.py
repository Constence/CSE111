# volumes.txt  


import math 
from datetime import datetime
print()
w = float(input('Enter the width of the tire in mm '))
print()
a = float(input('Enter the aspect ratio of the tire '))
print()
d = float(input('Enter the diameter of the wheel in inches '))


v_one = math.pi * w**2 * a 
v_two = v_one * (w * a + 2540 * d)
v = v_two / 10000000000
current_date_and_time = datetime.now()

print()
print(f"The approximate volume is {v:.2f} liters ")
print()
buy = input('Would you like to buy these tires [y/n]? ')

if buy.lower() == "y": 
    print() 
    number=input("Please type in your number so we can call you about billing")
    print()
    print("Thanks!")
    with open("volumes.txt", "at") as volumes_file:
        print(f"{ current_date_and_time:%Y-%m-%d}, { w} , { a} , { d} , { v:.2f} , { number} ", file=volumes_file)

else: 
    print() 
    print('Thats fine, have a good day')
    with open("volumes.txt", "at") as volumes_file:
        print(f"{ current_date_and_time:%Y-%m-%d}, { w} , { a} , { d} , { v:.2f} ", file=volumes_file)



