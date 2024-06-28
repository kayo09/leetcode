#incomplete, mf made me lose my streak
class Solution(object):
    def maximumImportance(self, n, roads):
        dic={}
        count=1
        for i in range(len(roads)):
            for j in range(len(roads[0])):
                if roads[i][j] not in dic:
                    count=1
                    dic[roads[i][j]]=count
                else:
                    count=dic[roads[i][j]]
                    dic[roads[i][j]]=count+1
        print(dic)


solution=Solution()
n=5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
solution.maximumImportance(n,roads)
               
