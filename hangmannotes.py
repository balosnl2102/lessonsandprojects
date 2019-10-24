myWord = "hello"

choice = input("Type a word: ")
if choice == myWord:
	print("It's a match")
else:
	print("Not a match")



# how to check if a letter is in a word

letter = input("Enter a letter: ")

if letter in myWord:
	print("Letter is in word")
else:
	print("Letter is not in word")

count = 0
for letter in myWord:
	if letter == choice:
		print(count)
	count == 1

# how to change a string into a list
myString = "Arizona"
mysteryWord = list(myString)
print(mysteryWord)
guessList = []

# How to make a list with '_' for characters
for letter in mysteryWord
	guessList.append("_")

print(guessList)

# How to replace a specific index in a list
guessList[3] = "z"

print(guessList)

secretWord = "Christmas"
secretWord = list(secretWord)
print(secretWord)
misses = 0
hangman = ["first Pic", "second Picture"]

guess = input("Guess a letter: ")

if guess in secretWord:
	print("letter in word")
else:
	misses = misses + 1

print("Misses: " + str(misses))
print(hangman[misses])