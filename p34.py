#variable lenght arguments.

def sum(*args):
	s=0
	

	for n in args:
		s=s+n
	return s
print(sum(2,10,))

def result(**kwargs):
	for subject in kwargs:
		return subject
print(result('math = 33' 'ds =34' ))