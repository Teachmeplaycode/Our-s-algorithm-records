def minWindow(s, t):
    if not s or not t or len(s) < len(t): return ""
    need={}
    for char in t:
        need[char]=need.get(char,0)+1
    left,right,vaild=0,0,0
    start=0
    min_len=float('inf')
    window={}
    while right < len(s):
        c = s[right]
        right+=1
        if c in need:
            window[c]=window.get(c,0)+1
            if window[c]==need[c]:
                vaild+=1
        while vaild==len(need):
            if right-left<min_len:
                start=left
                min_len=right-left
            d=s[left]
            left+=1
            if d in need:
                if window[d]==need[d]:
                    vaild-=1
                window[d]-=1
    return "" if min_len == float('inf') else s[start:start + min_len]
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # 输出: BANC