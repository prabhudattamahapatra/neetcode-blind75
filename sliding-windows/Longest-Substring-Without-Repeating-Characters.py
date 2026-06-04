class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            count=set()
            for j in range(i,len(s)):
                if s[j] in count:
                    break
                count.add(s[j])
            res=max(res,len(count))
        return res