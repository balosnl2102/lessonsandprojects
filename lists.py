favFoods = ["Pizza", "Ice Cream", "Noodles"]
print(favFoods[0])
print(favFoods[2])
print(favFoods)
# Adds to the end of the list
favFoods.append("Yogurt")
print(favFoods)
print("My 4th favorite food is " + favFoods[3])
# Adds to an index in a list
favFoods.insert(1, "Chicken")
print(favFoods)
# Remove an item from the list
favFoods.remove("Chicken")
print(favFoods)
# Remove by index
favFoods.pop(0)
print(favFoods)

favFoods.insert(0, "pizza")
# loop through a list
for food in favFoods:
	print(food)

numList = [3, 6, 2, 10, 12, 14, 69, 5]

# Loop through the list and add all the numbers together then print the sum

sum = 0
for num in numList:
	sum = sum + num

print(sum)
# Function to get the length of a list
print(len(numList))

# Make a list for favorite movies
# Prompt for a favorite movie

myFood = input("What is your favorite food? ")
favFoods.append(myFood)
favMovies = ["LaLaLand", "The Grinch", "Cars"]
myMovie = input("What is your favorite movie? ")
# List methods and functions
# append - adds an item to the end of a list
# insert - adds an item to a specified index
# remove - removes a specified item from a list
# pop - removes an item from a specified index
# len - returns the length of a list
print(favFoods[len(favFoods) - 1])