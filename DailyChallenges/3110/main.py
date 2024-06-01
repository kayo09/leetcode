class Solution(object):
    def scoreOfString(self, s):
        arr=list(s)
        score=0
        for i in range(0,len(arr)-1):
            score+=abs(ord(arr[i])-ord(arr[(i+1)%len(arr)]))
        return score
solution=Solution()
s="hello"
result=solution.scoreOfString(s)