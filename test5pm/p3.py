# python program to print fibanacci series using recursion.
n = int(input("Enter the number : "))
def feb(n):
    if n == 0 or n == 1:
        return n
    else:
        return feb(n-1)+feb(n-2)
print(feb(n))