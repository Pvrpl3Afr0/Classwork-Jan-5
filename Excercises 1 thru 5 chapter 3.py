#SAMPLE PROGRAM FROM BOOK BELOW:
'''
#This program simulates an elevator panel that skips the thirteenth floor.

#Obtain the floor number from the user as an int.
floor = int(input("Floor: "))

#Adjust floor if necessary.
if floor > 13:
    actualFloor = floor - 1
else:
    actualFloor = floor
#Print the result
print("The floor will travel to the actual floor", actualFloor)
'''
#Excercise 1, Skip both 13 and 14, unlucky
#To do this i can copy the stuff from above and insert another if statement.
floor = int(input("Floor: "))

#Adjust floor if necessary.
if floor == 13:
    actualFloor = floor - 1
elif floor == 14:
    actualFloor = floor - 2
else:
    actualFloor = floor - 1
#Print the result
print("The floor will travel to the actual floor", actualFloor)
'''
Note: This code is problematic because in real life there would be methods to
prevent access to these floors, therefore this imaginary elevator can easily
become confused
'''
#Excercise 2, consider the following:
'''
if originalPrice > 100:
    discountedPrice = originalPrice -10
else:
    discountedPrice = originalPrice - 20
If the price is less than 100, you get 20 dollars off. If the price is
over 100, you get 10 dollars off
95 would become 85
100 would become 90
105 would become 95.
'''
#Excercise 3, consider the following:
'''
if originalPrice < 100:
    discountedPrice = originalPrice -10
else:
    discountedPrice = originalPrice - 20
This time the two statements would ONLY output the same result if you input
both 100 or 110, both result in 90.
'''
#Excercise 4, consider the following:
'''
discountedPrice = originalPrice
if originalPrice > 100:
    discountedPrice = originalPrice - 10
95 would output 95
100 SHOULD output 100
105 would output 95
'''
#Excercise 5, Cars and stuff
fuelAmount = int(input("Input your fuel amount: "))
fuelCapacity = 100

if fuelAmount < fuelCapacity*.1:
    print("RED!")
else:
    print("Green!")
