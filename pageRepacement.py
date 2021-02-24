import random

def reformP(listp, num):
    old = 0
    for i in range(len(listp)):
        if i == num:
            old = listp[i][2]
            listp[i][2] = len(listp)
        for j in range(2,len(listp)+1):
            if (listp[i][2] == j) and (i != num) and (j > old):
                listp[i][2] = j-1
    return listp

def FIFO(process, page): 
    pageFaults = 0
    point = 0
    for i in range(len(page)):
        page[i].append(-1)

    #run algorithm
    for i in range(len(process)):
        status = 'F'
        if point == len(page):
            point = 0
        #check process in page
        for j in range(len(page)):
            if process[i] == page[j][1]:
                status =  'T'

        if status == 'T' :
            status = 'F'
        elif status == 'F' :
            for k in range(len(page)):
                if point == k :
                    page[k][1] = process[i] 
            point += 1
            pageFaults += 1 
        else :
            break
    print('pageFaults of FIFO algorithm = '+ str(pageFaults))

def Optiaml (process, page):
    pageFaults = 0
    #put process to fill page full
    for i in range(len(page)):
        page[i].append(-1)
    #run algorithm
    for i in range(len(process)):
        status = 'F'
        #check process in page
        for j in range(len(page)):
            if process[i] == page[j][1]:
                status =  'T'
        if status == 'T' :
            status = 'F'
        elif status == 'F' :
            count = []
            for z in range(len(page)):
                count.append(['count'+str(z)])
                count[z].append(0)
            #page
            for ps in range(len(page)):
                for pages in range(i, len(process)):
                    if page[ps][1] == process[pages]:
                        break
                    else :
                        count[ps][1] += 1
            fmaxs = []
            for fmax in range(len(page)):
                fmaxs.append(count[fmax][1])
            pt = 'N'
            for put in range(len(page)):
                if pt == 'N':
                    if max(fmaxs) == count[put][1] :
                        page[put][1] = process[i]
                        pageFaults += 1
                        pt = 'Y'

    print('pageFaults of OPTIMAL algorithm = '+ str(pageFaults))

def LRU(process, page):   
    pageFaults = 0
    #put process to fill page full
    for i in range(len(page)):
        page[i].append(-1)
        page[i].append(i+1)

    #run algorithm
    for i in range(len(process)):
        k = -1
        status = 'F'
        #check process in page
        for j in range(len(page)):
            if process[i] == page[j][1]:
                k, status = j, 'T'
        if status == 'T' :
            page = reformP(page,k)
            status = 'F'
        
        else :
            check, nx = 'nothing', 0
            for x in range(len(page)):
                if page[x][2] == 1:
                    page[x][1] = process[i]
                    check, nx = 'change', x
            if check == 'change':
                page = reformP(page, nx)
            pageFaults += 1 
        
    print('pageFaults of LRU algorithm = '+ str(pageFaults))

    
    

# process = [10, 3, 2, 14, 3, 6, 2, 1, 2, 12, 6, 1, 15, 15, 1, 0, 10, 15, 11, 0, 6, 4, 10, 4, 8, 
# 11, 11, 14, 11, 11, 5, 2, 7, 13, 1, 9, 8, 4, 2, 8, 13, 15, 7, 14, 1, 9, 8, 9, 10, 1, 3, 15, 13, 14, 12, 0, 6, 4, 1, 1, 7, 7, 15, 5, 3, 11, 15, 4, 10, 3]
# main
# set input
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
FIFO(process, page)

# clear page before run OPTIMAL algorithm
page = []
for i in range (frame):
    page.append([str(i)])
Optiaml(process, page)

# clear page before run LRU algorithm
page = []
for i in range (frame):
    page.append([str(i)])
LRU(process, page)


