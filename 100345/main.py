class Solution(object):
    def minimumOperations(self, nums):
        operation=0
        for i in range(len(nums)):
            if nums[i]%3==0:
                pass
            elif( nums[i]+1)%3==0:
                operation+=1
            elif (nums[i]-1)%3==0:
                operation+=1
        return operation
    



solution=Solution()
nums=[3,6,9]
result=solution.minimumOperations(nums)
print(result)