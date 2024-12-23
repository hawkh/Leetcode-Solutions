import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int t=s.nextInt();
        for(int tc=0;tc<t;tc++){
            int n=s.nextInt();
            System.out.printf("Case #%d:\n",tc+1);
            for(int j=0;j<2*n;j++){
                for(int k=0;k<2*n;k++){
                    if((j/2+k/2)%2==0){
                        System.out.print("*");
                    }
                    else{
                        System.out.print("-");
                    }
                }
                System.out.println();
            }
            
        }
    }
}
