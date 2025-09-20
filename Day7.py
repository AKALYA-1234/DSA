# Sum of first n natural numbers using while loop

n = int(input("Enter the number: "))
i = 1
total = 0
while i <= n:
    total += i   
    i += 1       

print(f"Sum of first {n} natural numbers = {total}")