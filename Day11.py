#Check Palindrome & GCD Or HCF

import math
def is_palindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    return n == rev

def find_gcd(a, b):
    return math.gcd(a, b)

choice = int(input("Enter 1 for Palindrome Check,2 for GCD/HCF: "))

if choice == 1:
    num = int(input("Enter a number:"))
    if is_palindrome(num):
        print(num, "is a Palindrome")
    else:
        print(num, "is NOT a Palindrome")

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD / HCF of", a, "and", b, "is:",find_gcd(a, b))

else:
    print("Invalid choice!")