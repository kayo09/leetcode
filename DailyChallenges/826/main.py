# mf broke my streak 
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        initial_profit=0
        rating={}
        for diff in range(len(difficulty)):
            rating[difficulty[diff]]=profit[diff]
        for work in range(len(worker)):
            for i in rating.keys():
                if i <worker[work]:
                    initial_profit+=rating[i]
                   
        print(initial_profit)
        # print(rating)

                    



        
solution=Solution()
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
solution.maxProfitAssignment(difficulty, profit, worker) 

