
# how to use range and for loops when calling functions: 
import random 
#draws on cloud
#  
def draw_cloud(canvas, width, height, x_min, x_max, y_min, y_max):
    for i in range (0,4): 
        x_start = random.randRange(x_min, x_max)
        y_start = random.randRange(y_min, y_max)
#draws multiple clouds 

def draw_clouds(number_of_clouds): 
    for i in range ( 0 , number_of_clouds): 
        draw_cloud(...)
###################################################################

# return gets data out of a fuction 
import math 
def calc_ciricle_area(radius): # this is a argument 
    return radius**2 * math.pi 

area = calc_ciricle_area(5) 

user_input = input("please enter a number") # this is a peramiters 

print (user_input)
print (area)

##############################################################

#to call a funtion you need to say th def and then put in the arguments 
str = "bob"

#print every other letter in a string 

str_length = len (str)

print (str_length)

#############################################################

friuts = ["apple", "orange"]
your_fruits = ['bannana', 'pear']
friuts.extend[your_fruits]
new_fruit = ["grape"]
friuts.extend[new_fruit]
print(friuts)

for i in range (len(friuts)): 
    print(friuts[i])

# or you could do this for no ''

friuts_string  = ', '.join(friuts)

print(friuts_string)