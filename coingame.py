# Coin Game 
# You are given two piles of coins where Pile A has x coins, and Pile B has y coins. In each turn, you can either pick 2 coins from Pile A and 1 coin from Pile B or 1 coin from Pile A and 2 coins from Pile B. Check whether it is possible to empty both the piles or not.



# Input Format

# The first line of input contains an integer T. In the next T lines, you are given two spaced separated integers x and y.



# Output Format

# Print "YES" if you can empty both the piles, otherwise print "NO".



# Constraints

# 1 <= T <= 105

# 0 <= x, y <= 107



# Example

# Input

# 3

# 1 2

# 4 2

# 8 12



# Output

# YES

# YES

# NO



# Explanation



# Self Explanatory

def empty(t,tc):
    res=[]
    for x,y in tc:
        if (x+y)%3==0 and max(x,y)<=2*min(x,y):
            res.append("YES")
        else:
            res.append("NO")
    return res

t=int(input())
tc=[tuple(map(int,input().split())) for _ in range(t)]
res=empty(t,tc)
print("\n".join(res))
