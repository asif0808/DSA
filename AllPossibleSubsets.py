#this program is for returning all possible subsets of a given array/list
a=[2,3,4,12,7,8,10]
n=len(a)
for i in range(n):
    for j in range(i,n):
        print(a[i:j+1])