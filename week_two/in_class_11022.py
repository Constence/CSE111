
import math 

def compute_cirlce_area(radius): 
    area = radius**2 * math.pi
    return area

def promt_user_for_rad(): 
    user_radius = float(input("please enter a radius ")) 
    return user_radius

def display_area(area): 
    print(area) 

area = round(compute_cirlce_area(), 2)

display_area(area)

#global ver. is when ver. will be avaible for all to use 
#functions have their own function scope, so they dont care about other ver. 
