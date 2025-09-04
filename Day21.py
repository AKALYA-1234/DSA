# Fibonacci Number

n=int(input("Enter the number of fibonacci terms:"))
a=0
b=1
print("Fibonacci sequence:")
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b
