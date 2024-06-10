class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in dic: 
                [dic[diff],i]
            else:
                dic[nums[i]]=i
        print(dic)








solution=Solution()
nums = [3,2,4]
target = 6 
result=solution.twoSum(nums,target)
print(result)
