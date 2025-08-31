#Pattern DSA

#Right Triangle Star Pattern:

n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    

#Inverted Triangle:
n=int(input("Enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#Number pattern:

n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Inverted Number pattern:

n=int(input("Enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()