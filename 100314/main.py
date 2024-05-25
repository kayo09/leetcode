class Solution(object):
    numLine=[0]
    results=[]
    def getResults(self, queries):
        sz=0
        obstacle=0
        for row,rowValue in enumerate(queries):
            for column,columnValue in enumerate(queries[row]):
                if(columnValue==1 and column==0):
                    obstacle=queries[(columnValue+1)%len(queries[row])]
                    self.numLine.append(obstacle)
                    self.results.append(False)
                    break
                sz=queries[row][len(queries[row])-1]

                for num in self.numLine:
                    print(num)
            print(sz)
solution=Solution()
queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
solution.getResults(queries)