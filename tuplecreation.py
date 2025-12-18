my_tuple = ()

n = int(input("Enter number of elements: "))

temp = []

for i in range(n):
    value = input(f"Enter element {i+1}: ")
    temp.append(value)

my_tuple = tuple(temp)

print("Created Tuple:", my_tuple)
