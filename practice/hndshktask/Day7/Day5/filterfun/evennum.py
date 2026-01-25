#filter even numbers from given list using filter()function.
mylist = [66,65,44,4,8,78,53,34]
def filter_even(n):
    if n % 2 == 0:
        return True
even_numbers = list(filter(filter_even,mylist))
#print(list(even_numbers))
print(even_numbers)
print(type(even_numbers))
#print(list(even_numbers))
print(even_numbers)