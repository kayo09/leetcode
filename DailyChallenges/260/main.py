class Solution(object):
    def singleNumber(self, nums):
        self.nums=sorted(nums)
        output=[]
        for num in nums: 
            if num not in output:
                output.append(num)
            else: output.remove(num)
        return output
    
solution= Solution()
nums = [1,2,1,3,2,5]
result=solution.singleNumber(nums)
