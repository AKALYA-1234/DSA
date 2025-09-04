#Count digits & Reverse the number:

n=int(input("Enter the number:"))
count=0
temp=n
while temp>0:
    count+=1
    temp//=10
print(count)
rev=0
temp=n
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
print("Revesed Number:",rev)
