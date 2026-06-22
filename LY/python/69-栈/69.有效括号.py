class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:return False
        if s[0] in [')', ']', '}']: return False
        st_push = ['(', '[', '{']
        st_pop = [')', ']', '}']
        match_mp = {'(':')', '[':']', '{':'}'}
        st = []
        for ch in s:
            if ch in st_push:st.append(ch)
            if ch in st_pop:
                if len(st) == 0:return False
                cur = st[-1]
                if cur in match_mp and match_mp[cur] != ch:return False
                else:st.pop()
        return True if len(st) == 0 else False
class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:return False
        match_mp = {'(':')', '[':']', '{':'}'}
        st = []
        for ch in s:
            if ch in match_mp:st.append(ch)
            else:
                if not st or match_mp[st[-1]] != ch:return False
                st.pop()
        return not st
sol = Solution()
s1="()"
s2="()[]{}"
s3="(]"
s4="([)]"
s5="{[]}"
s6=")"
s7="("
s8="}[]"
s9="()}{}()"
for i in [s1,s2,s3,s4,s5,s6,s7,s8,s9]:print(sol.isValid(i))