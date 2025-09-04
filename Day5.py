#Array:
n=int(input("Enter the number:"))
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
print(arr)
print(sum(arr))

#String:
a=input("Enter a string:")
vowels="aeiou"
count=0
for ch in a:
    if ch in vowels:
        count+=1
print("Total Vowels:",count)