# volumes.txt  


import math 

w = float(input('Enter the width of the tire in mm '))
a = float(input('Enter the aspect ratio of the tire '))
d = float(input('Enter the diameter of the wheel in inches '))


v_one = math.pi * w**2 * a 
v_two = v_one * (w * a + 2540 * d)
v = v_two / 10000000000


print(f"The approximate volume is {v:.2f} liters")
