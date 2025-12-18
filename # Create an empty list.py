# Create an empty list
my_list = []

# Take number of elements from user
n = int(input("Enter number of elements: "))

# Add elements to the list
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

# Display the list
print("The created list is:", my_list)
