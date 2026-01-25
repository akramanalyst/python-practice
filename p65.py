# import sys

import sys
num_lst = [x for x in range(100)]
num_gen = (x for x in range(100))

print(sys.getsizeof(num_lst))
print(sys.getsizeof(num_gen))