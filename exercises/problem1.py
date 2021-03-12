#Write a program that does the following:

#Asks a user to enter a number "x"
#Asks the user to  enter a number "y"
#Prints out number "x", raised to the power "y"
#Prints out the log(base 2) of "x"

from library import math
print("Please enter a number 'x' ")
x = input()
x = float(x)

print("Please enter a number 'y' ")
y = input()
y = float(y)

exp = x ** y
lgrm = math.log2(x)


print(f"The number 'x' raised to the power of 'y' is {exp}, and ...")
print(f"The log(base 2) of x is {lgrm}")
