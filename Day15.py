def print_n_times(name,n):
    if n==0:
        return
    print(name)
    print_n_times(name,n-1)
    
num=int(input("Enter how many times:"))
print_n_times("Hello",num)