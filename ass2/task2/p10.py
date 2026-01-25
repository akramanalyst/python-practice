# reverse of number

#123 => 321

n = int(input(" enter a number : "))
rev = 0
while n > 0:
	r = n%10 # 3 ..#2...#1
	rev = rev*10+r # 3#....30+2=32...320+1=321
	n = n//10 # ..12..#..1
print(rev)