
def partition(tab,start,end):
    r = tab[end]
    stepper = start
    for i in range(start,end+1):
        if tab[i]<=r:
            tmp = tab[stepper]
            tab[stepper] = tab[i]
            tab[i] = tmp
            stepper+=1
    return stepper-1

tab = [2,8,7,1,3,5,6,4]
            
    

def quicksort(tab,start,end):
    if end-start <1:return
    part_index = partition(tab,start,end)
    quicksort(tab,start,part_index-1)
    quicksort(tab,part_index+1,end)
    
quicksort(tab,0,len(tab)-1)
print(tab)