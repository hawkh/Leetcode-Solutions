class Solution:
    def getMaximumGold(self, g: List[List[int]]) -> int:
        h,w = len(g),len(g[0])
        def f(i,j):
            if h>i>-1<j<w and g[i][j]:
                x = g[i][j]
                g[i][j] = 0
                c = max(map(f,(i+1,i-1,i,i),(j,j,j+1,j-1)))
                g[i][j] = x
                return c+x
            return 0
        return max(f(i,j)for i in range(h)for j in range(w))
