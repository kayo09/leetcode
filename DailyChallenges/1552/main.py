class Solution(object):
    def maxDistance(self, position, m):
        def canPlace(distance):
            count=1
            last=position[0]
            for pos in position[1:]:
                if pos - last>= distance:
                    count+=1
                    last=pos
                    if count==m:
                        return True
            return False
            
        position.sort()
        left=1
        right=position[-1]-position[0]

        #little binary search 🤌🏾
        while left<=right:
            mid=(left+right)//2
            if canPlace(mid):
                left=mid+1
            else: 
                right=mid-1
        return right 






solution=Solution()
# position=[5,4,3,2,1,10000]
position=[1,2,3,4,7]
m=3 
result=solution.maxDistance(position,m)
print(result)
