
my_list = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

print("List:", my_list)
index = int(input("Enter index to access element: "))

if 0 <= index < len(my_list):
    print("Element at index", index, "is:", my_list[index])
else:
    print("Invalid index")
