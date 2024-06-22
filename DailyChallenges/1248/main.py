class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        """
        odds=[]
        count=0
        sub_arr=0
        for num in nums: 
            if(num%2!=0):
                odds.append(int('1'))
            else: 
                odds.append(int('0'))
        for odd in range(len(odds)):
            count+=odd
        print(count)






            

        


solution=Solution()
nums=[2,2,2,1,2,2,1,2,2,2]
k=3
solution.numberOfSubarrays(nums,k)