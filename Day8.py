#Pass by Value
def change_number(x):
    x = x + 5
    print("Inside function:", x)

num = int(input("Enter a number: "))
change_number(num)
print("Outside function:", num)

#Pass by Reference
def change_list(lst):
    lst.append(100)
    print("Inside function:", lst)

numbers = []
n = int(input("How many numbers? "))

for i in range(n):
    val = int(input(f"Enter number {i+1}: "))
    numbers.append(val)

change_list(numbers)
print("Outside function:", numbers)