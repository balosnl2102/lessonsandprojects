# Calaculations, printing, variables

# Printing to the screen
# The built in function print(), prints to the screen
# it will print both Strings and numbers
print("Printing to the screen...")
print("hello")# a string
print('hello again')
print(6) # a number
print("6") # string again
print(6 + 6) # 12
print("6" + "6") # string concationation

# Performing Calculations
# addition +
# subtraction -
# multiplication *
# division /
# exponents **
# modulo %

print(4 - 2) # subtraction -> 2
print(4*2) # multiplication -> 8
print(4 / 3) # division -> 1.333...
print(4 ** 3) # exponents -> 64
print("Modulo operator test...")
print(5 % 3)
print(10 % 2)
print(16 % 3)
# Modulo gives remainders
# python operators follow the same order of operations as Math
print(4 - 2 * 2) # should give zero
print((4 - 2) * 2) # should give 4

# variables
# variables are used to hold data
# variables are declared and set to a value (initializing)
badLuck = 13 # declared a variable called badLuck and initialized it to 13
# I can print the variable using it's name 
print("badLuck = " + str(badLuck)) # cast it to a string
# lets do another one
goodLuck = "4" # String variable
print("goodLuck = " + goodLuck) # don't have to cast
badLuck + 5 # this is pointless
print(badLuck)
badLuck = badLuck + 5 # now badLuck is 18
print(badLuck)

# you can also save input variables
# using input(), A prompt goes inside the ()
name = input("What is your name? ")
print("Hello" + name)
print(name * 10)
name = name + "\n" # escape character (newline)
print(name * 10)
# lets try some math
base = input("Enter the base number: ")
exp = input("Enter the exponent: ")
print(int(base) ** int(exp))