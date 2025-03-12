def Parent(i):
    return i//2
def Left(i):
    return 2*i
def Right(i):
    return 2*i+1

def max_heapify(heap,i,heap_size):
    l= Left(i)
    r = Right(i)
    if l<= heap_size and heap[l]>heap[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and heap[r]>heap[largest]:
        largest = r
    if largest !=i:
        tmp = heap[i]
        heap[i] = heap[largest]
        heap[largest] = tmp
        max_heapify(heap,largest,heap_size)
        
        
def build_max_heap(heap,heap_size):
    for i in range(heap_size//2,0,-1):
        max_heapify(heap,i,heap_size)
    

def heap_sort(heap):
    build_max_heap(heap,len(heap)-1)
    heap_size = len(heap)
    for i in range(len(heap)-1,1,-1):
        tmp = heap[1]
        heap[1] = heap[i]
        heap[i] = tmp
        heap_size-=1
        max_heapify(heap,1,heap_size-1)
        
        

    
# heap = [0,16,4,10,14,7,9,3,2,8,1] 
heap = [0,4,1,3,2,16,9,10,14,8,7]    
print(heap)        
heap_sort(heap)
print(heap)        




    