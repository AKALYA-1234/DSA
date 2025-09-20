#check if the number is prime or not

num=int(input("Enter the number:"))
flag=1
for i in range (2,num):
    if(num%i==0):
        flag=0
        break
    else:
        flag=1

if(flag==1):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")