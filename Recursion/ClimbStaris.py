#climb the stairs problem indicates that a person can climb one or two step at a time so return how many ways a person can climb to the given number of stairs

def ClimbStairs(n):
    if(n==0 or n==1):
        return 1
    return ClimbStairs(n-1)+ClimbStairs(n-2)
print(ClimbStairs(4))