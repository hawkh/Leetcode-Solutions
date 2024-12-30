# Longest Prefix Suffix 
# Given a string, compute the length of the longest proper prefix which is same as the suffix of the given string.



# Input Format

# The input contains a string S, consisting of only lowercase characters.



# Output Format

# Print the length of the longest proper prefix which is the same as a suffix of the given string.



# Constraints

# 1 <= len(S) <= 100



# Example

# Input

# smartintsmart



# Output

# 5



# Explanation



# Self Explanatory

def kmp(s):
    n=len(s)
    lps=[0]*n
    l=0
    i=1
    while i<n:
        if s[i]==s[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
    return lps[-1]

s=input().strip()
print(kmp(s))
