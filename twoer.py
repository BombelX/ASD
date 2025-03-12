#ludzie i schodki rozne wysokosci ludzi i schodków

def binary_search():
    return 1


def tower(humans,stairs):
    S = 0
    m = len(humans)
    n = len(stairs)
    tab_max = [0]*(n+1)
    for i in range(1,n):
        tab_max[i]=max(stairs[i],tab_max[i-1])
    for i in range(m):
        id_max = binary_search(tab_max,humans[i])
        S+= id_max
    return S

