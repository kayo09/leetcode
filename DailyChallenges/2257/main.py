from typing import List
class Solution(object):
    def countUnguarded(self,m:int,n:int,guards:List[List[int]],walls:List[List[int]]):
        g=[[0]*n for _ in range(m)]
        for x,y in guards:
            g[x][y]=2
        for x,y in walls:
            g[x][y]=2

        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        for gx,gy in guards:
            for dx,dy in directions: 
                x,y=gx,gy
                while True:
                    x+=dx
                    y+=dy
                    if x<0 or x>=m or y<0 or y>=n or g[x][y]==2:
                        break
                    g[x][y]=1
        return sum(row.count(0) for row in g)



m:int=4
n:int=6
guards:List[List[int]]=[[0,0],[1,1],[2,3]]
walls:List[List[int]]=[[0,1],[2,2],[1,4]]
solution=Solution()

stat=solution.countUnguarded(m,n,guards,walls)
print(stat)


