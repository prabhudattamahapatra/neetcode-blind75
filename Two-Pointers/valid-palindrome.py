class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=""
        for i in s:
            if i.isalnum():
                clean+=i.lower()
        left=0
        right=len(clean)-1
        isPalindrome=True
        while left<right:
            if clean[left]!=clean[right]:
                isPalindrome=False
                break
            left+=1
            right-=1
        return isPalindrome
            

