#pre easy, since the cetral node is going to have the node most
#common vertex 

class Solution(object):
    def findCenter(self, edges):
        freq={}
        count=0
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                if edges[i][j] in freq:
                    count=freq.get(edges[i][j])+1
                    freq[edges[i][j]]=count
                else:
                    count=0
                    freq[edges[i][j]]=count+1
        return (max(freq,key=freq.get))


    

solution=Solution()
edges= [[1,3],[3,2],[4,3]]
solution.findCenter(edges)
