package hoot100;

import java.util.*;

public class Test {
    public static void main(String[] args) {
        ListNode head=new ListNode(1);
        head.next=new ListNode(2);
        head.next.next=new ListNode(2);
        head.next.next.next=new ListNode(1);
        Solution solution=new Solution();
        boolean result = solution.isPalindrome(head);
        System.out.println(result);
    }

}
//双指针解法
class ListNode{
    int val;
    ListNode next;
    ListNode(int x){this.val=val;}
}
class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> vals = new ArrayList<Integer>();
        ListNode currentNode=head;
        while(currentNode!=null){
            vals.add(currentNode.val);
            currentNode=currentNode.next;
        }

        //双指针
        int front=0;
        int back=vals.size()-1;
        while (front<back){
            if(!vals.get(front).equals(vals.get(back))){
                return false;
            }
            front++;
            back--;
        }
        return true;
    }
}
