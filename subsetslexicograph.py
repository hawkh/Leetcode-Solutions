def subs(ar,temp,idx):
    if(temp!=None and temp!=[]):
        print(*temp)
    for i in range(idx,len(ar)):
        temp.append(ar[i])
        subs(ar,temp,i+1)
        temp.pop()
    return 

def sub(a):
    temp=[]
    subs(a,temp,0)

T=int(input())
for i in range(T):
    n=int(input())
    ar=list(map(int,input().split()))
    ar.sort()
    sub(ar)
