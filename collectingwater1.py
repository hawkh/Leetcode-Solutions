T=int(input())
for _ in range(T):
    n=int(input())
    h=list(map(int,input().split()))
    lm=[0]*n
    rm=[0]*n
    lm[0]=h[0]
    for i in range(1,n):
        lm[i]=max(lm[i-1],h[i])
    rm[n-1]=h[n-1]
    for i in range(n-2,-1,-1):
        rm[i]=max(rm[i+1],h[i])
    ans=0
    for i in range(1,n-1):
        ans+=(min(lm[i],rm[i])-h[i])
    print(ans)
