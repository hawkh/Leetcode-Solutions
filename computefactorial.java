import java.io.*;
import java.util.*;

public class Main {
    static long mod=(long)1e9+7;
    static int max_n=1000000;
    static long[] fact=new long[max_n];
    static{
        fact[0]=1;
        fact[1]=1;
        for(int i=2;i<max_n;i++){
            fact[i]=(fact[i-1]*(long)i)%mod;
        }
    }

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int t=s.nextInt();
        for(int i=0;i<t;i++){
            int n=s.nextInt();
            
            System.out.println(fact[n]);
        }
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Main. */
    }
}