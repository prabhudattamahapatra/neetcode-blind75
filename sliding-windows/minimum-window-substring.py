class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result=""
        
            
            
        for i in range(len(s)):
            temp=""
            for j in range(i,len(s)):
                temp+=s[j]
                valid=True
                for ch in set(t):
                    if temp.count(ch) < t.count(ch):
                        valid=False
                        break
                if valid:
                    if result=="" or len(temp)<len(result):
                        result=temp
        return result