import heapq
def find(nums,k):
    min_heap=[]
    for num in nums:
        heapq.heappush(min_heap,num)
        #print(min_heap)
        if(len(min_heap)>k):
           # print('popped')
            heapq.heappop(min_heap)
    return min_heap[0]
print(find([2,4,5,1,9],1))
