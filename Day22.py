#Happy number check

n = int(input("Enter the number: "))

class Solution(object):
    def isHappy(self, n):
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        seen = set()  
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

solution = Solution()

if solution.isHappy(n):
    print(f"{n} is a Happy Number")
else:
    print(f"{n} is not a Happy Number")
