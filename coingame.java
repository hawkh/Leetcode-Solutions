// //Coin Game 
// You are given two piles of coins where Pile A has x coins, and Pile B has y coins. In each turn, you can either pick 2 coins from Pile A and 1 coin from Pile B or 1 coin from Pile A and 2 coins from Pile B. Check whether it is possible to empty both the piles or not.



// Input Format

// The first line of input contains an integer T. In the next T lines, you are given two spaced separated integers x and y.



// Output Format

// Print "YES" if you can empty both the piles, otherwise print "NO".



// Constraints

// 1 <= T <= 105

// 0 <= x, y <= 107



// Example

// Input

// 3

// 1 2

// 4 2

// 8 12



// Output

// YES

// YES

// NO



// Explanation



// Self Explanatory




import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
    Scanner s=new Scanner(System.in);
    int t=s.nextInt();
    while(t-->0){
        int x=s.nextInt();
        int y=s.nextInt();
        if(2*x-y  >=0 && 2*y-x>=0 && (x+y)%3==0){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
    
    }
}
