#mf broke my streak
#these last 3-4 challenges have been kicking ass, i have also been busy 
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        flower=0
        wait=0
        for i in range(len(bloomDay)):
            wait=bloomDay[i]
            if wait>i:
                flower+=1
solution=Solution()
bloomDay=[1,10,3,10,2]
m=3
k=2
solution.minDays(bloomDay,m,k)
        
