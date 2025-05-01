#this is a more optimised way as compared to brute force because it take O(n^2 logn) time complexity
#first step is to sort the array (sort() has timecomplexity of O(nlogn))
a=[1,2,2,1,1]
a.sort()
#print(a)
freq=1
for i in range(1,len(a)):
    if(a[i]==a[i-1]):
        freq+=1
    else:
        freq=1
    if(freq>len(a)/2):
        print("majority element is: ",a[i], "no. of occurences are: ",freq)
        break;