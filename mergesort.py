def merge(arr,l,m,r):
    larr=arr[l:m+1]
    rarr=arr[m+1:r+1]
    i=j=0
    k=l
    while i<len(larr) and j<len(rarr):
        if larr[i]<=rarr[j]:
            arr[k]=larr[i]
            i+=1
        else:
            arr[k]=rarr[j]
            j+=1
        k+=1
    while i<len(larr):
        arr[k]=larr[i]
        i+=1
        k+=1
    while j<len(rarr):
        arr[k]=rarr[j]
        j+=1
        k+=1

    print(" ".join(map(str,arr)))
def msort(arr,l,r):
    if l<r:
        m=(l+r)//2
        msort(arr,l,m)
        msort(arr,m+1,r)
        merge(arr,l,m,r)

n=int(input())
arr=list(map(int,input().split()))
msort(arr,0,n-1)
