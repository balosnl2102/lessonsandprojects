# Name: Nathan Balos
# Period 1
# Dice Rolling Simulator
import random
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
cChoices = ["1", "2", "3", "4", "5", "6"]
print("\n")
print("Welcome to Dice Roller!")
loopNumber = input("How many 6-sided dice rolls will be performed?")
print("\n")
a=0
while a < int(loopNumber):
	rollnumber = random.choice(cChoices)
	print("Roll number : " + str(a + 1))
	if rollnumber == "1":
		ones = ones + 1
		print("Dice landed on 1")
	elif rollnumber == "2":
		twos = twos + 1
		print("Dice landed on 2")
	elif rollnumber == "3":
		threes = threes +1
		print("Dice landed on 3")
	elif rollnumber == "4":
		fours = fours + 1
		print("Dice landed on 4")
	elif rollnumber == "5":
		fives = fives + 1
		print("Dice landed on 5")
	elif rollnumber == "6":
		sixes = sixes + 1
		print("Dice landed on 6")
	print("1s - " + str(ones))
	print("2s - " + str(twos))
	print("3s - " + str(threes))
	print("4s - " + str(fours))
	print("5s - " + str(fives))
	print("6s - " + str(sixes))
	a=a+1
	print("\n")
print("Total Rolls: " + str(a))
print("1s - " + str(ones))
print("2s - " + str(twos))
print("3s - " + str(threes))
print("4s - " + str(fours))
print("5s - " + str(fives))
print("6s - " + str(sixes))
print("\n")
print("Percentages: ")
ones = (int(ones))/(int(loopNumber) / 100)
print("1s - " + str(ones) + "%")
twos = (int(twos))/(int(loopNumber) / 100)
print("2s - " + str(twos) + "%")
threes = (int(threes))/(int(loopNumber) / 100)
print("3s - " + str(threes) + "%")
fours = (int(fours))/(int(loopNumber) / 100)
print("4s - " + str(fours) + "%")
fives = (int(fives))/(int(loopNumber) / 100)
print("5s - " + str(fives) + "%")
sixes = (int(sixes))/(int(loopNumber) / 100)
print("6s - " + str(sixes) + "%")
print("\n")
print("We hope we were able to be of service!")
print("\n")