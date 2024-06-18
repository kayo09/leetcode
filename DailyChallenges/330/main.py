"""
input nums and n
process patches required for nums to have all elements [1,n] inclusive 

to do: 
    break the array nums such that break
"""
class Solution(object):
    def minPatches(self, nums, n):
        #after patch
        #check if sequence ⊆ [1,n]
        patch=0
        dic={}
        arr=list([i for i in range(1,n+1)])
        for i in arr:
            sum=i
            for j in range(len(nums)) :
        


            

            
        print(dic)

                

          

solution=Solution()
nums=[1,3]
n=6
solution.minPatches(nums,n)