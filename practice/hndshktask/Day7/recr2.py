# python program to print numbers fro n to 1.
n = int(input("Enter the value of n : "))
def numbers(n):
    if n == 0 : 
        return
    print(n)
    return numbers(n-1)
numbers(n)