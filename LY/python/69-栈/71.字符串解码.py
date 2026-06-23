class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            right = s.index(']')
            left = s.rfind('[', 0, right)
            inner = s[left+1:right]
            num_start = left - 1
            while num_start >= 0 and s[num_start].isdigit():
                num_start -= 1
            num_start += 1 
            chr = int(s[num_start:left])
            process = inner * chr
            s = s[:num_start] + process + s[right+1:]
        return s
sol = Solution()
s = "200x2[xyz]"
print(sol.decodeString(s))
