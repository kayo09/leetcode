class Solution(object):
    def reverseString(self, s):
            
        left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s 



solution=Solution()
s = ["h","e","l","l","o"]
results=solution.reverseString(s)
print(results)
