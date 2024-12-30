# Arrange Primes 
# Given an integer N. Print the count of permutations for the numbers from 1 to N, considering that prime numbers should be placed at positions with prime indices (1 - based indexing). As the result might be a large number, print the output % 1e9 + 7.



# Input Format

# The first and only line of input contains an integer N.



# Output Format

# Print the count of permutations.



# Constraints

# 1 ≤ N ≤ 100



# Example

# Input

# 8



# Output

# 576



# Explanation



# Self Explanatory

mod=int(1e9+7)
def fact(n):
    res=1
    for i in range(2,n+1):
        res=(res*i)%mod
    return res

def sieve(n):
    isprime=[True]*(n+1)
    isprime[0]=isprime[1]=False
    for i in range(2,int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i,n+1,i):
                isprime[j]=False
    return isprime

def arrange(n):
    isprime=sieve(n)
    primecnt=sum(1 for i in range(1,n+1)if isprime[i])
    nonprimecnt=n-primecnt

    primefact=fact(primecnt)
    nonprimefact=fact(nonprimecnt)
    return (primefact*nonprimefact)%mod

n=int(input())
print(arrange(n))
