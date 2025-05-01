#majority element is the one which occurs more than n/2 times (where n is total no. of elements)
#this is the bruteforce approach for finding majority element
a=[1,2,2,1,1]
for i in range(len(a)):
    freq=0
    for j in range(len(a)):
        if a[j]==a[i]:
            freq+=1
    if freq>len(a)/2:
        print("Majority Element ->", a[i],"Occurence ->", freq)
        break;
#not an optimised way because it takes O(n^2) time complexity