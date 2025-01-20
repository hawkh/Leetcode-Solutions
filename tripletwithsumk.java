// Triplet with Sum K 
// You are given an integer array and a positive integer K. You have to tell if there exists i,j,k in the given array such that ar[i]+ar[j]+ar[k]=K, i≠j≠k.



// Input Format

// The first line of input contains T - the number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array.



// Output Format

// For each test case, print "true" if the arrays contains such elements, "false" otherwise, separated by new line.



// Constraints

// 30 points

// 1 <= T <= 100

// 3 <= N <= 100



// 70 points

// 1 <= T <= 100

// 3 <= N <= 1000



// General Constraints

// -105 <= A[i] <= 105

// 0 <= K <= 105



// Example

// Input

// 3

// 5 60

// 1 20 40 100 80

// 12 54

// 12 45 52 65 21 645 234 -100 14 575 -80 112

// 3 15

// 5 5 5



// Output

// false

// true

// true



// Explanation



// Self Explanatory
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
      Scanner s=new Scanner(System.in);
      int t=s.nextInt();
      while(t-->0){
          int n=s.nextInt();
           int k=s.nextInt();
           int[] a=new int[n];
           for(int i=0;i<n;i++){
               a[i]=s.nextInt();
           }
           boolean ans=cs(a,k,n);
           System.out.println(ans);
      }
    }
    public static boolean cs(int[] a,int k,int n){
        for(int i=0;i<n-2;i++){
            int ts=k-a[i];
            HashSet<Integer> set=new HashSet<>();
            for(int j=i+1;j<n;j++){
                if(set.contains(ts-a[j])){
                    return true;
                }
                set.add(a[j]);

            }

        }
        return false;
    }
}
