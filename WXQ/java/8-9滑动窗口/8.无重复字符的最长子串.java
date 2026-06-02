import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Test3 {
    public static void main(String[] args) {
        String s="abcabcbb";
    }
}
class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] ss=s.toCharArray();
        Set<Character> set=new HashSet<>();
        int res=0;
        for (int left=0,right=0;right<s.length();right++){
            char ch=ss[right];
            while(set.contains(ch)){
                set.remove(ss[left]);
                left++;
            }
            set.add(ch);
            res=Math.max(res,right-left+1);
        }
        return res;
    }
}

