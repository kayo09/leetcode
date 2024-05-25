class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        results=[]
        occurrences = []
        for i, num in enumerate(nums):
            if num == x:
                occurrences.append(i)
        for q in queries:
            if q <= len(occurrences):
                results.append(occurrences[q-1])
            else:
                results.append(-1)
        
        return results

solution=Solution()
nums= [1,3,1,7]
queries= [1,3,2,4]
x=1
result=solution.occurrencesOfElement(nums,queries,x)
print(result)