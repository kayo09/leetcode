class Solution(object):
    def longestSubarray(self, nums, limit):
        subarray=[]
        for i in range(len(nums)):
            subarray.append(nums[i])
            diff=abs(nums[i]-subarray[i])
            print(diff,subarray)






solution=Solution()
nums=[8,2,4,7]
limit=4
solution.longestSubarray(nums,limit)
