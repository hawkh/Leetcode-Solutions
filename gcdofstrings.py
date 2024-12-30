# String GCD 
# Given two strings, P and Q, your task is to find the largest common divisor string S, such that both P and Q are divisible by S. In other words, there exists a string 'S' for which P = S + S + ... + S and Q = S + S + ... + S. If such a string S exists, output the largest possible S, otherwise, print -1.



# Note: A string X is divisible by string Y if and only if X can be obtained by concatenating Y with itself one or more times.



# Input Format

# The first line of input contains the string P. The Second line of input contains string Q.



# Output Format

# Print the largest string S.



# Constraints

# 1 ≤ len(P), len(Q) ≤ 1000

# 'A' <= P[i],Q[i] <= 'Z'



# Example

# Input

# ABABAB

# ABAB



# Output

# AB



# Explanation



# Self Explanatory


def gcd(p,q):
    if p+q!=q+p:
        return -1
    import math
    gcd_len=math.gcd(len(p),len(q))
    gcd_str=p[:gcd_len]
    return gcd_str
p=input().strip()
q=input().strip()
res=gcd(p,q)
print(res)
