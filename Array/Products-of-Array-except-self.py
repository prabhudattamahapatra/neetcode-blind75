class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        
        for i in range(len(nums)):
            count=1
            for j in range(len(nums)):
                if j==i:
                    continue
                count=count*nums[j]
            result.append(count)
        return result