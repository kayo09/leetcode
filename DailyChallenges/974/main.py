class Solution(object):
    def subarraysDivByK(self, nums, k):
        dic={0:1}
        running_sum=0
        count=0
        
        for num in nums:
            running_sum+=num
            mod=running_sum%k
            if mod <0:
                mod+=k
            if mod in dic: 
                count+=dic[mod]
                dic[mod]+=1
            else:
                dic[mod]=1
        return count










solution=Solution()
nums = [4,5,0,-2,-3,1]
k = 5
solution.subarraysDivByK(nums,k)
