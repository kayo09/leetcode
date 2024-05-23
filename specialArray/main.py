class Solution(object):
    def isArraySpecial(self, nums):
        boolVal=True

        for i,num in enumerate(nums):
            if(len(nums)==1):
                break

            thisElem=num
            #nextelement should not be first element
            nextElem=nums[(i+1)%len(nums)]
            if(nextElem==nums[0]):
                break
            if((thisElem%2==0 and nextElem%2!=0) or (thisElem%2!=0 and nextElem%2==0)):
                continue 
            else:
                boolVal=False
        return boolVal        
    
nums=[2,1,4]
va=Solution.isArraySpecial(Solution,nums)
print(str(va))