#Excercises 8-12
import math
import pi
#Excercise 8
balance = input("Insert initial balance: ")
bal = float(balance)

percent = input("Insert percentage of interest: ")
per = float(percent)
years = input("How many years will we be calculated? Insert here: ")
yr = int(years)
total = (bal*per)*yr

print("After ", yr, "Years, you will gain: ", total)

#Excercise 9

area_of_square = input("Insert the area of a square: ") #This value will work if it's not a float but it should be a float anyway
area = float(area_of_square)#This converts the value from above into a float
root = sqrt(area)#This takes the obtained value and sqrt it
print("The side length of a square with an area of ", area, "Will be: ", root)
#The side length of a square with an area of 64 will be 8.0

#Excercise 10 volume :(
radius = input("Insert the radius: ")
rad = float(radius)
p = pi

print("Your volume is: ", (4/3)*p*rad**3)
#Excercise 11

print(1729//10) #172
print(1729%10) #9

#Excercise 12
number = input("Insert a number: ")
n = int(number)
if n > 0:
    print("Your number is: ", (n//10)%10)
else:
    print("Error!")
