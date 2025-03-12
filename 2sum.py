# for for n^2
# sort bin
# gasienicowe sort + n

def sum2(T,x):
    T = sorted(T)
    l,r = 0,len(T)
    while l<r:
        if T[l]+T[r] == x:
            return l,r
        
        