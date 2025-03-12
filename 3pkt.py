def three_point_on_the_line(tab):  # wersja bez słownika O(n^2 * log(n)) 
    size = len(tab)
    for i in range(size):        
        wspołczynniki_kierunkowe = []
        for j in range(i+1,size):
            # print(tab[j],tab[i])
            if tab[j][0] != tab[i][0]:
                p = (tab[j][1] - tab[i][1])
                q = (tab[j][0] - tab[i][0])
                a = p/q  # a = (y_b - y_a)/(x_b - x_a) wzor na wspolczynnik kierunkowy
                wspołczynniki_kierunkowe.append(a)
        wspołczynniki_kierunkowe.sort
        
        for x in range(0,len(wspołczynniki_kierunkowe)-1):
            if abs(wspołczynniki_kierunkowe[x+1] - wspołczynniki_kierunkowe[x])<0.05:
                return True
    return False
          
          
points = [(1, 2), (2, 4), (3, 1), (0,0),(3, 6)]  
res = three_point_on_the_line(points)

print(res)
            

