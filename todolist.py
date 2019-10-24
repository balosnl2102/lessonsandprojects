print("Welcome to To Do List")
todolist = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Choose: ")
	if choice == "q":
		break
	elif choice == "a":
		#add an item to the list
		additem = input("What item would you like to add to the list?")
		additemspot = input("What rank/position will this item have on the list? (1,2,3,etc.)")
		additemspot = int(additemspot) - 1
		todolist.insert(int(additemspot), str(additem))
	elif choice == "r":
		removeitem = input("What item would you like to remove from the list?")
		todolist.remove(removeitem)
	elif choice == "p":
		print(todolist)
	else:
		print("You chose something not listed")