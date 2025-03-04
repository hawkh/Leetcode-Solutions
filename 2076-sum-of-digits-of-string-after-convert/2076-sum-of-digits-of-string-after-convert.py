class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=''
        for i in s:
            num+=str(ord(i)-ord('a')+1)
        while k>0:
            temp=0
            for j in num:
                temp+=int(j)
            num=str(temp)
            k-=1
        return int(num)


