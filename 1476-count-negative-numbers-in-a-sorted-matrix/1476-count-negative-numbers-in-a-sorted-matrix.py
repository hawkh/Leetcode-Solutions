class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cn=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]<0):
                    cn+=1
        return cn

        