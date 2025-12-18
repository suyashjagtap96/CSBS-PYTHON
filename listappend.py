my_list = []

n = int(input("Enter number of elements to append: "))

for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    my_list.append(value)

print("List after appending elements:", my_list)
