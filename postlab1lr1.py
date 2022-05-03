# mean of array    
def mean(a):
    x=len(a)
    sum=0
    for i in a:
        sum=sum+i;
    return sum/x

# median of array 
def med(a):
    a.sort()
    x=len(a)
    mid=int(x/2);
    if(x%2==1):
        return a[mid]
    else:
        return (a[mid]+a[mid+1])/2

# mode of array 
def mode(a):
    res = max(set(a), key = a.count)
    return res
    
# from stats import median,mode,mean 

lyst=[1,3,2,6,7,5,9,8,5,4]

print(mean(lyst))
print(mode(lyst))
print(med(lyst))