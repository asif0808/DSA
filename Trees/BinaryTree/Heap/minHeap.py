import heapq
min_heap=[]
heapq.heappush(min_heap,10)
heapq.heappush(min_heap,15)
heapq.heappush(min_heap,4)
heapq.heappush(min_heap,1)
heapq.heappush(min_heap,18)
print(min_heap)
#peak element
print(min_heap[0])
#remove smallest element
print('popped element: ',heapq.heappop(min_heap))
print(min_heap)
print(type(min_heap))