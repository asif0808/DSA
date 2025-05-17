import heapq
max_heap=[]
heapq.heappush(max_heap,-10)
heapq.heappush(max_heap,-15)
heapq.heappush(max_heap,-4)
heapq.heappush(max_heap,-1)
heapq.heappush(max_heap,-18)
print([-x for x in max_heap])
#peak element
print(-max_heap[0])
#remove smallest element
print('popped element: ',-heapq.heappop(max_heap))
print([-x for x in max_heap])
print(type(max_heap))