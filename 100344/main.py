class Solution(object):
    def minOperations(self, nums):
            
        
        operations=0
        n=len(nums)
        for i in range(n-2):
            if nums[i]==0:
                nums[i]^=1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                operations += 1
        if any(x==0 for x in nums[-2:]):
            return -1
        
        return operations
                
      



solution=Solution()        
nums = [0,1,1,1,0,0]
result=solution.minOperations(nums)
print(result)