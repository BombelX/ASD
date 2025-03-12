

def merge(t1,t2):
    i1,i2 = 0,0
    n = len(t1)
    res = [0]*(2*n)
    for i in range(2*n):    
        if i1>=n:
            res[i] = t2[i2]
            i2 += 1
        elif i2>=n:
            res[i] = t1[i1]
            i1 += 1    
        elif t1[i1]<t2[i2]:
            res[i] = t1[i1]
            i1+=1
        else:
            res[i] = t2[i2]
            i2+=1 
    return res



def divide(tab):
    n = len(tab)
    if n!=1:
        t1 = divide(tab[0:(n)//2])
        t2 = divide(tab[(n//2):n])
        return merge(t1,t2)
    else:
        return tab
def merge_sort(tab):
    sorted = divide(tab)
    return sorted


print(merge_sort([1,6,2,4,11,1,123,3]))

