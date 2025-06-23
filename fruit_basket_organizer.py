# List of fruits as tuples (NAME, COLOUR)
fruit_basket = [
    ("Apple", "Red"),
    ("Banana", "Yellow"),
    ("Cherry", "Red"),
    ("Grapes", "Green"),
    ("Strawberry", "Red"),
    ("Orange", "Orange"),
    ("Blueberry", "Blue"),
    ("Watermelon", "Green")
]

# Convert color to lowercase for case-insensitive comparison
# Using list comprehension to filter red fruits
red_fruits = [fruit for fruit in fruit_basket if fruit[1].lower() == "red"]

# Display all fruits
print("All Fruits in Basket:")
for fruit in fruit_basket:
    print(fruit)

# Display filtered red fruits
print("\nRed Fruits:")
for fruit in red_fruits:
    print(fruit)