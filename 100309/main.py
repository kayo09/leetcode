class Solution(object):
    def duplicateNumbersXOR(self, nums):
        count={}
        xor_result=0

        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num,count in count.items():
            if count>1:
                xor_result^=num
        return xor_result
solution=Solution()
nums= [1,2,2,1]

result=solution.duplicateNumbersXOR(nums)
print(result)