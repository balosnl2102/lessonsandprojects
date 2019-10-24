#conditionals

age = input("What is your age?") # prompt for age

# check if the age is more that 17, so the person
# can see R rated parents
age= int(age)
if age > 17: #everything in the if statement only runs if the condition is true
	print( "You can see an R rated movie")

else:
	print( "You cannot see an R rated movie, too bad so sad")

print("Have a nice day")
# you can check all these conditions
# >, <, >=, <=, == (== means equal to)

birthday = input( "Is today your birthday ( yes or no)?")
if birthday == "yes":
	print("Happy Birthday!")
print("Have a nice day.")

myNum = 7
guess = input("Guess a number between 1 and 10?")
guess = int(guess)
if guess == myNum:
	print("You guessed correctly!")
elif guess > myNum:
	print("Too High")
else: 
	print("Too Low")
print("Thanks for playing")
