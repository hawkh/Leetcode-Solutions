# Frequency Sort 
# You are given an array of integers. Sort them by frequency. See examples for more clarifications.



# Input Format

# The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.



# Output Format

# For each test case, print the elements of the array sorted by frequency. In case 2 elements have the same frequency, print the smaller element first.



# Constraints

# 1 <= T <= 100

# 1 <= N <= 10000

# -1000 <= A[i] <= 1000



# Example

# Input

# 2

# 6

# 4 -2 10 12 -8 4

# 8

# 176 -272 -272 -45 269 -327 -945 176



# Output

# -8 -2 10 12 4 4

# -945 -327 -45 269 -272 -272 176 176



# Explanation



# Self Explanatory

from collections import Counter
T=int(input())
for i in range(T):
    n=int(input())
    ar=list(map(int,input().split()))
    ar.sort()
    d=Counter(ar)
    def counts(val):
        return d[val]
    ar.sort(key=counts)
    print(*ar)
