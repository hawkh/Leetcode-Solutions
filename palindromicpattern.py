# Palindromic Pattern 
# Print a palindromic right-angled triangle pattern using characters. See the example for more details.



# Input Format

# The first and only line of input contains an integer N - the size of the pattern.



# Output Format

# For the given integer N, print the palindromic right-angled triangle pattern.



# Constraints

# 1 <= N <= 26



# Example

# Input

# 5



# Output

# A

# A B A

# A B C B A

# A B C D C B A

# A B C D E D C B A



# Explanation



# Self Explanatory


n=int(input())
for i in range(1,n+1):
    inc=[chr(65+j) for j in range(i)]
    dec=inc[-2::-1]
    print(" ".join(inc+dec))
    
