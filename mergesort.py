from linkedlist import *
import time
file = open('unsorted-data/unsorted-10000.txt', 'r')
numbers = [int(numbers_temp) for numbers_temp in file.read().strip().split(' ')]
file.close()

def mergeSort(d):
    data = d
    if len(data) <= 1:
        return data
    l2 = data.split()
    l1 = data
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    result = merge(l1, l2)
    return result

def merge(l1, l2):
    result = LinkedList()
    len1 = len(l1)
    len2 = len(l2)
    while (len1 >= 1 and len2 >= 1):
        c1 = l1.firstNode
        c2 = l2.firstNode
        if c1.value < c2.value:
            result.append(c1.value)
            l1.removeFirst()
            len1 -= 1
        else:
            result.append(c2.value)
            l2.removeFirst()
            len2 -= 1
    len3 = len(result)
    if len1 > len2:
        last = result.look(len3-1)
        last.nextNode = l1.firstNode
        l1.firstNode.lastNode = last
    elif len1>len2:
        last = result.look(len3-1)
        last.nextNode = l2.firstNode
        l2.firstNode.lastNode = last
    return result

l = LinkedList()
for n in numbers:
    l.append(n)
t1 = time.time()
mergeSort(l)
t2 = time.time()
print('This sorting procedure took %s seconds' % (t2-t1))