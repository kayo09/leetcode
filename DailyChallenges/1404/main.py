class Solution(object):
    step=0
    # def numSteps(self, s):
    #     if isinstance(s, str):
    #         s = int(s, 2)
    #     if s == 1:
    #         return self.step
        
    #     if s % 2 == 0:
    #         s = s // 2
    #     else:
    #         s += 1  
        
    #     self.step += 1
        
    #     return self.numSteps(s)
  
    def numSteps(self, s):
        if isinstance(s, str):
            s = int(s, 2)  
        
        while s != 1:
            if s % 2 == 0:
                s //= 2  
                s += 1  
            self.step += 1  
        
        return self.step


solution=Solution()
s="1"
results=solution.numSteps(s)
print(results)
