class Solution(object):
    def minIncrementForUnique(self, nums):
          nums.sort()
          track=0
          minIncrement=0
          for num in nums:
              track=max(track,num)
              minIncrement+=track-num
              track+=1
          return minIncrement
            


          
                    

        
solution=Solution()
nums = [3,2,1,2,1,7]
solution.minIncrementForUnique(nums)
