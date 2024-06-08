class Solution(object):
    def checkSubarraySum(self, nums, k):

        #felt cheeky might delete later ;)
        dic={0:-1}
        running_sum=0
        for i,num in enumerate(nums):
            running_sum+=num
            remainder=running_sum%k
            if remainder<0:
                remainder+=k
            
            if remainder in dic:
                #checks if the subarray is at least of len 2
                if i-dic[remainder] >1:
                    return True
            else:
                dic[remainder]=i
        return False









        
solution=Solution()
nums = [23,2,4,6,7]
k = 6
results=solution.checkSubarraySum(nums,k)
print(results)
