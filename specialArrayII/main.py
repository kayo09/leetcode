class Solution(object):
    def isArraySpecial(self, nums, queries):
        start=0
        checker=[]
        for i in range(0,len(queries)):
            for j in range(0,len(queries[0])):
                if(j%2==0):
                    start=queries[i][j]
                    end=queries[i][(j+1)%len(queries[0])]
                    subarray=nums[start:end+1]
                    checker.append(self.checkSpecial(subarray))
        return checker

    def checkSpecial(self,subarray):
        isSpecial=False
        if(len(subarray)==1):
            isSpecial=True 
        for i in range(len(subarray)-1):
            isSpecial=False 
            if(len(subarray)==1):
               isSpecial=True 
            if(subarray[i]%2==0 and subarray[i+1]%2!=0) or (subarray[i]%2!=0 and subarray[i+1]%2==0):
               isSpecial=True 
            if(isSpecial==False):
                break
        return isSpecial
                

        
nums=[3,7,8]
queries= [[0,2]]
solution=Solution()
result= solution.isArraySpecial(nums,queries)
print(result)