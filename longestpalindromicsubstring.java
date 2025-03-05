import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            sc.nextLine();
            int res=Integer.MIN_VALUE;
            String k=sc.nextLine();
            char[] s=k.toCharArray();
            int p1=0,p2=0;
            for(int i=0;i<n;i++){
                p1=i;
                p2=i+1;
                while(p1>=0 && p2<n && s[p1]==s[p2]){
                    p1--;
                    p2++;
                }
                res=Math.max(res,p2-p1-1);
                p1=i;p2=i;
                while(p1>=0 && p2<n && s[p1]==s[p2]){
                    p1--;
                    p2++;
                }
                res=Math.max(res,p2-p1-1);
            }
            System.out.println(res);
        }

         }
    }
