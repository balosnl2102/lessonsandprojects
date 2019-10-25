import random
myWords = ["awkward", "bagpipes", "banjo", "bungler","croquet","crypt","dwarves","fervid","fishhook","fjord","gazebo","gypsy","haiku","haphazard","hyphen","ivory","jazzy","jiffy","jinx","jukebox","kayak","kiosk","klutz","memento","mystify","numbskull","ostracize","oxygen","pajama","phlegm","pixel","polka","quad","quip","rhythmic","rogue","sphinx","squawk","swivel","toady","twelfth","unzip","waxy","wildebeest","yacht","zealous","zigzag","zippy","zombie"]
hangmanword = random.choice(myWords)
mysteryWord = list(hangmanword)

guessList = []

for letter in mysteryWord:
	guessList.append("_")

guessList = list(guessList)

print(guessList)
incorrectGuesses = []
guessMax = input("How many misses will you allow yourself?")
guessNumber = 0
while guessNumber < int(guessMax):
	if "_" not in guessList:
		print("Congratulations, you have won!")
		break
	if "_" in guessList:
		guess = input("Enter a letter: ")
		if guess in mysteryWord:
			print("Letter is in word")
			count = 0
			for letter in mysteryWord:
				if letter == guess:
					guessList[count] = guess
					print(guessList)
				count += 1
		else:
			print("Letter is not in word")
			guessNumber = guessNumber + 1
			incorrectGuesses.append(guess)
			print("Missed letters: " + str(incorrectGuesses))

guessNumber = guessNumber + 1
if guessNumber > int(guessMax):
	print("You have lost, try again next time!")