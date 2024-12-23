import java.io.*;
import java.util.*;
class Node{
    int data;
    Node right,left;
    public Node(int data){
        this.data=data;
        this.right=null;
        this.left=null;
    }
}

public class Main {
    public static Node insert(Node root,int data){
        if(root==null){
            root=new Node(data);
            return root;
        }
        if(data<root.data){
            root.left=insert(root.left,data);
        }
        else if(data>root.data){
            root.right=insert(root.right,data);
        }
        return root;
    }
    
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int t=s.nextInt();
        while(t-->0){
            int n=s.nextInt();
            int[] a=new int[n];
            for(int i=0;i<n;i++){
                a[i]=s.nextInt();
            }
            Node root=null;
            for(int i=0;i<n;i++){
                root=insert(root,a[i]);
            }


        }
    }
    }
