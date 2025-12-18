my_list = []

n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

print("Original List:", my_list)

index = int(input("Enter index to change element: "))

if 0 <= index < len(my_list):
    new_value = int(input("Enter new value: "))
    my_list[index] = new_value
    print("Updated List:", my_list)
else:
    print("Invalid index")
