class Solution(object):
    numLine=[0]
    def getResults(self, queries):
        for row,rowValue in enumerate(queries):
            for column,columnValue in enumerate(queries[row]):
                if(columnValue==1 and column==0):
                    blockVal=queries[(columnValue+1)%len(queries[row])]
                    self.numLine.append(blockVal)

                    print(self.numLine)
                # print(column,columnValue)

solution=Solution()
queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
solution.getResults(queries)