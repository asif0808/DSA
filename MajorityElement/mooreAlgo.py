#this is the most optimised approach with time complexity of O(n) and space complexity of O(1)
a=[1,2,2,1,1,]
ans=0
freq=0
for i in range(len(a)):
    if(freq==0):
        ans=a[i]
    if(ans==a[i]):
        freq+=1
    else:
        freq-=1
print(ans)