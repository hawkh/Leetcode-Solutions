import java.io.*;
import java.util.*;

public class Main {
    static boolean diff(int n,long arr[],int k){
        Arrays.sort(arr);
        int i=0;
        int j=0;
        while( i<n && j<n){
            if(arr[j]-arr[i]==k && i!=j) return true;
            else if(arr[j]-arr[i]<k){j++; continue;}
            i++;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int t=s.nextInt();
        while(t--!=0){
            int n=s.nextInt();
            int k=s.nextInt();
            long arr[]=new long[n];
            for(int i=0;i<n;i++){
                arr[i]=s.nextLong();
            }
            System.out.println(diff(n,arr,k));
        }
        
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Main. */
    }
}
