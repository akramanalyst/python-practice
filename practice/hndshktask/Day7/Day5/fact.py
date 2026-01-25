num = int(input("Enter the number to find factorial  : "))
def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)

print(fact(num))