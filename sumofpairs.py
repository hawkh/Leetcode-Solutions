
def binsearch(ar,n,l,h,k):
    while(l<=h):
        mid=l+(h-l)//2
        if(ar[mid]==k):
            return True
        elif(ar[mid]<k):
            l=mid+1
        else:
            h=mid-1
    return False
def pairsum(ar,n,tar):
    ar.sort()
    for i in range(n):
        k=binsearch(ar,n,i+1,n-1,tar-ar[i])
        if k:
            return True
    return False

T=int(input())
for i in range(T):
    n,k=map(int,input().split())
    ar=list(map(int,input().split()))
    print(pairsum(ar,n,k))
