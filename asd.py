def maxrank(T):
    if not T:
        return 0

    # Kompresja współrzędnych
    unique_vals = sorted(set(T))
    comp = {v: i+1 for i, v in enumerate(unique_vals)}  # mapowanie wartości na indeksy od 1 do m
    m = len(unique_vals)
    
    # Inicjalizacja BIT
    BIT = [0] * (m + 1)
    
    def update(i, delta):
        while i <= m:
            BIT[i] += delta
            i += i & -i
    
    def query(i):
        s = 0
        while i > 0:
            s += BIT[i]
            i -= i & -i
        return s
    
    max_rank = 0
    # Przetwarzanie tablicy T
    for x in T:
        idx = comp[x]
        # Liczba elementów mniejszych od x
        r = query(idx - 1)
        max_rank = max(max_rank, r)
        update(idx, 1)
    
    return max_rank

# Przykład użycia:
T = [5, 3, 9, 4]
print(maxrank(T))  # Wynik: 2
