# Trailing Zeros Modified 
# Given an integer N, print the number of positive integers whose factorial ends with N 0's.



# Input Format

# The first line of input contains T - number of test cases. Its followed by T lines, each containing an integer N.



# Output Format

# For each test case, print the number of positive integers whose factorial ends with N 0's, separated by newline.



# Constraints

# 30 points

# 1 <= T <= 100

# 0 <= N <= 104



# 70 points

# 1 <= T <= 1000

# 0 <= N <= 1014



# Example

# Input

# 3

# 1

# 5

# 2



# Output

# 5

# 0

# 5



# Explanation



# Test Case 1:

# The positive integers whose factorial ends with one 0 are: 5, 6, 7, 8, 9



# Test Case 2:

# There are no positive integers whose factorial ends with five 0's.



# Test Case 3:

# The positive integers whose factorial ends with two 0's are: 10, 11, 12, 13, 14

def trailing_zeros(x):
    res = 0
    while x > 0:
        x = x // 5
        res += x
    return res

def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    for N in cases:
        if N == 0:
            print(4)
            continue
        low = 0
        high = 5 * N
        while low < high:
            mid = (low + high) // 2
            tz = trailing_zeros(mid)
            if tz < N:
                low = mid + 1
            else:
                high = mid
        x_min = low
        tz_xmin = trailing_zeros(x_min)
        if tz_xmin != N:
            print(0)
        else:
            if x_min == 0:
                print(5)
            else:
                tz_prev = trailing_zeros(x_min - 1)
                print(5 if tz_prev < N else 0)

main()
