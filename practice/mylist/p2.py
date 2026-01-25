
my_list = ['apple','orange','banana','graps','kiwi']
print(my_list)
print('       ')
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print('       ')
print(my_list[-1])
print('      ')

print(my_list[1:4])
print('     ')

print(my_list[0:5:2])
print('    ')
my_list.append('pinaple')
print(my_list)

print('   ')
print(my_list[:4])
print('   ')
print(my_list[::-1])
print('   ')
my_list.insert(2,'cherry')
print(my_list)

print('    ')
print(' .........extend the list with another list........ ')
print('    ')
lst = [ 1,2,3,4,5,6,7,8,9 ]
my_list.extend(lst)
print(my_list)
print('    ')
print(' ....... reverse the list....... ')
print('    ')
my_list.reverse()
print(my_list)
print('     ')
print(' ......... find index of elements.....')
print('     ')
index = my_list.index('graps')
print(index)
index = my_list.index(5)
print(index)
print('     ')
print('.....sorting elemetns of list ....')
numbers = [ 2,3,4,5,1,45,6,8,2,4,5,6,8,45,2,4,45,45]

numbers.sort()
print(numbers)
print('      ')
print('......counting the elements......')
count1 = numbers.count(2)
count2= numbers.count(4)
count3= numbers.count(45)
print(count1,count2,count3)   

print(45 in numbers)

print('    ')
num1 = [3,4,5]
num2 = [1,2,6,7]
numbers2 = num1+num2
print(numbers2)
print('    ')
numbers2.sort()
print(numbers2)

print('    ')
print(' using for loop : ')
for fruit in my_list:
	print(fruit)

print('     ')
for number in numbers:
	print(number)

print('    ')
print(' pop method : remove elements from last. ')
numbers.pop()
print(numbers)

print('    ')
numbers.pop(0)
print(numbers)
print('    ')
numbers.pop(4)
print(numbers)
numbers.pop(2)
print(numbers)
print('     ')
print(" list repetative elements : " )
list1 = num1*2
print(list1)

print('      ')
print(".....while loop........")
i = 0
while i <len(numbers):
	print(numbers[i])
	i=i+1