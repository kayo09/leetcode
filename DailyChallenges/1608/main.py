class Solution(object):
    def specialArray(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i] >= i + 1 and (i == len(nums) - 1 or nums[i + 1] < i + 1):
                return i + 1
        return -1
        

               

        
solution=Solution()
nums=[3,9,7,8,3,8,6,6]

results=solution.specialArray(nums)
print(results)