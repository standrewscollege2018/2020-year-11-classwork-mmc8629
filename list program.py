"""this program demonstrates how lists work, including how to print, change and append lists"""
#lists always have square brackets. Items are seperated by commas
fruit = ["apples", "Oranges", "kiwifruit", "Bananas"]

#to print an item form a list, use the name of the lists
print(fruit[0])

# you can print the entrie list
print(fruit)

# len(list()) gives the number of times in the list
print(len(fruit))

#to change an item in a list, just use its index and set it directly
fruit[0] = "mango"

# to insert an item at a specific location, use insert(index, item)
fruit.insert(3, "apple")

# its often easier to just add a new item to the end of a list
# to do this, we use append()
fruit.append("Dragonfruit")
