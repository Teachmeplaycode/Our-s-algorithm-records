class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:return False
        match_mp = {'(':')'}
        st = []
        for ch in s:
            if ch in match_mp:st.append(ch)
            else:
                if not st or match_mp[st[-1]] != ch:return False
                st.pop()
        return not st
    def longestValidParentheses(self, s: str) -> int:
        if s == '':return 0
        ans = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if self.isValid(s[i:j+1]):ans = max(len(s[i:j+1]),ans)
        return ans
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':st.append(i)
            elif len(st) > 1:
                st.pop()
                ans = max(ans, i - st[-1])
            else:st[0] = i
        return ans
sol = Solution()
s = "(()"
print(sol.longestValidParentheses(s))