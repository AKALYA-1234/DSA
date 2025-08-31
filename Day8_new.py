#Cheak palindrome

def is_armstrong(num):
    temp = num
    digits = len(str(num)) 
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return num == total

num = int(input("Enter a number:"))

if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
