import time

file = open('unsorted-data/unsorted-10000.txt')
numbers = [int(numbers_temp) for numbers_temp in file.read().strip().split(' ')]
file.close()
t1 = time.time()
running = True
count = 1
while running:
    found = 0
    for x in range(0, len(numbers)-count):
        n1 = numbers[x]
        n2 = numbers[x+1]
        if n1 > n2:
            numbers[x+1] = n1
            numbers[x] = n2
            found += 1
    count += 1
    if found == 0:
        running = False
        break
t2 = time.time()
print(numbers)
print('This operation took me %s seconds' % (t2-t1))