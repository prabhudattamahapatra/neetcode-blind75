class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    right-=1
        unique_list=[]
        for i in result:
            if i not in unique_list:
                unique_list.append(i)
        return unique_list

                