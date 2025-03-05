def largestnondivsubset(t,tc):
    res=[]
    for cas in tc:
        n,k,arr=cas
        cnt=[0]*k
        for num in arr:
            rem=num%k
            cnt[rem]+=1
        size=min(cnt[0],1)
        for i in range(1,(k//2)+1):
            if i==k-i:
                size+=min(cnt[i],1)
            else:
                size+=max(cnt[i],cnt[k-i])
        res.append(size)
    return res



t=int(input())
tc=[]
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    tc.append((n,k,arr))
res=largestnondivsubset(t,tc)
for i in res:
    print(i)
