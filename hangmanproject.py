import random
myWords = ["awkward", "bagpipes", "banjo", "bungler","croquet","crypt","dwarves","fervid","fishhook","fjord","gazebo","gypsy","haiku","haphazard","hyphen","ivory","jazzy","jiffy","jinx","jukebox","kayak","kiosk","klutz","memento","mystify","numbskull","ostracize","oxygen","pajama","phlegm","pixel","polka","quad","quip","rhythmic","rogue","sphinx","squawk","swivel","toady","twelfth","unzip","waxy","wildebeest","yacht","zealous","zigzag","zippy","zombie"]
hangmanword = random.choice(myWords)
letterList = ['''_''']
correctLetters = []

myString = (hangmanword)
mysteryWord = list(myString)
guessList = []

for letter in mysteryWord:
	guessList.append("_")

for letter in mysteryWord:
	print(letterList, end="")
	correctLetters.append(letter in hangmanword)
guessNumber = 0
guessMax = input("How many misses will you allow yourself?")

while guessNumber < int(guessMax)
	letterGuess = input("Guess a letter: ")
	if letterGuess in mysteryWord:
		mysteryWord.insert(letterGuess == mysteryWord[], letterGuess)

while guessNumber < int(guessMax):
	letterGuess = input("Guess a letter: ")
	if letterGuess == mysteryWord[0]:
		mysteryWord.insert(0, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(1)
	elif letterGuess == mysteryWord[1]:
		mysteryWord.insert(1, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(2)
	elif letterGuess == mysteryWord[2]:
		mysteryWord.insert(2, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(3)
	elif letterGuess == mysteryWord[3]:
		mysteryWord.insert(3, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(4)
	elif letterGuess == mysteryWord[4]:
		mysteryWord.insert(4, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(5)
	elif letterGuess == mysteryWord[5]:
		mysteryWord.insert(5, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(6)
	elif letterGuess == mysteryWord[6]:
		mysteryWord.insert(6, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(7)
	elif letterGuess == mysteryWord[7]:
		mysteryWord.insert(7, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(8)
	elif letterGuess == mysteryWord[8]:
		mysteryWord.insert(8, letterGuess)
		print(mysteryWord)
		mysteryWord.pop(9)
	else:
		guessNumber = guessNumber + 1

#print(len(hangmanword))