#this problem is about buying and selling a stock such that u gain the maximum profit (Time Complexity- O(n))
a=[7,1,5,3,6,4]
mp=0
bestbuy=a[0]
for i in range(1,len(a)):
    if(a[i]>bestbuy):
        mp=max(mp,a[i]-bestbuy)
    bestbuy=min(bestbuy,a[i])
print(bestbuy,mp)


