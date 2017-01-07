#Excercises 22-26

#Excercise 22, write a prompt for users age

Age = input("What is your age? Input it here: ")
age = int(Age)

print("Your age is ", age)

#Excercise 23, What is problematic about the following?
'''
userInput = input("Please enter the unit price: ")
unitPrice = int(userInput)
It seems that this code makes the unit price an integer which may not
always be the case, you can have floats as prices.
Besides that, the code does what it's supposed to.
'''

#Excercise 24, What is problematic about the following?
'''
userInput = input("Please enter the number of cans: ")
cans = int(userInput)
A bad habit in variable naming could be having the I in userInput capitalized.
Instead, it could be something like user_input
'''
#Excercise 25, What is the output of the following?
volume = 10
print("The volume is %5d" % volume)
#This outputs the previously defined volume by calling upon it and adds five
#spaces in front
# The volume is     10
#Excercise 26, string format operators

bottles = 8
cans = 24

print("Bottles: %5d" % bottles)
print("Cans: %8d" % cans)
