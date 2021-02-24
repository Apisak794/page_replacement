import random
import Function as Fn

# setup input
print('How many capacity of process : ')
cap = int(input())
print('How many frame : ')
frame = int(input())

# random process
process = []
for c in range(cap):
    process.append(random.randrange(0, 10))
print('')
print('process =',process)

# clear page before run FIFO algorithm
page = []
for i in range (frame):
    page.append([str(i)])
Fn.FIFO(process, page)

# clear page before run OPTIMAL algorithm
page = []
for i in range (frame):
    page.append([str(i)])
Fn.Optiaml(process, page)

# clear page before run LRU algorithm
page = []
for i in range (frame):
    page.append([str(i)])
Fn.LRU(process, page)