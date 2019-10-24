import time
import os

frameList = ['''
  +---+
  o   |
 /|\  |
 / \  |
     ===
 ''',
 '''
  +---+
 \o/  |
  |   |
 / \  |
     ===''',
 '''
  +---+
 \o/  |
  |   |
   \  |
     ===''',
 '''
  +---+
 \o/  |
  |   |
      |
     ===''',
 '''
  +---+
  o/  |
  |   |
      |
     ===''',
 '''
  +---+
  o   |
  |   |
      |
     ===''',
 '''
  +---+
  o   |
      |
      |
     ===''',
 '''
  +---+
      |
      |
      |
     ===''']

while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(.3)
		os.system("cls")