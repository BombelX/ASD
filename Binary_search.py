def find(T):
    n = len(T)
    l=0
    r = n-1
    m = (l+r)//2
    while (l<r):
        m = (l+r)//2
        if m == T[m]:
            l = n+1
        else:
            r=m
    return l+1

T = [0,1,2,3,5,8]