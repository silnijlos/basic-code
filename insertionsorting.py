from linkedlist import *
import time

file = open('unsorted-data/unsorted-20000.txt', 'r')
numbers = [int(numbers_temp) for numbers_temp in file.read().strip().split(' ')]
file.close()

l = LinkedList(numbers[0])
del numbers[0]
t1 = time.time()
for n in numbers:
    l.sortedInsert(n)
t2 = time.time()
print('This operation took %s seconds' % (t2-t1))