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

    