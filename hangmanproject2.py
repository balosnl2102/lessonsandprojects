myString = "computer"
mysteryWord = list(myString)
guessList = []

for letter in mysteryWord:
	guessList.append("_")

print(guessList)
incorrectGuesses = []
guessMax = input("How many misses will you allow yourself?")
guessNumber = 0
while guessNumber < int(guessMax):
	letter = input("Enter a letter: ")
	if letter in mysteryWord:
		print("Letter is in word")
	else:
		print("Letter is not in word")
		guessNumber = guessNumber + 1
		incorrectGuesses.append(letter)
		print("Missed letters: " + str(incorrectGuesses))