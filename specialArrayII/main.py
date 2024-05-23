class Solution(object):
    def isArraySpecial(self, nums, queries):
        start=0
        checker=[]
        for i in range(0,len(queries)):
            for j in range(0,len(queries[0])):
                if(j%2==0):
                    start=queries[i][j]
                subarray=nums[start:queries[i][j]+1]
                checker.append(self.checkSpecial(subarray))
        return checker

    def checkSpecial(subarray):
        for i in range(len(subarray)-1):
            if(len(subarray)==1):
                return True
            elif(subarray[i]%2==0 and subarray[i+1]%2!=0) or (subarray[i]%2!=0 and subarray[i+1]%2==0):
                return True
        return False
                

        
nums= [4,3,1,6]
queries= [[0,2],[2,3]]
solution= Solution.isArraySpecial(Solution,nums,queries)
print(solution)