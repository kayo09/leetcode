class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        #using some slick dictionary compression out here :P
        rank= {val:i for i, val in enumerate(arr2)}
        arr1.sort(key=lambda x: (rank.get(x,len(arr2)),x))
        return arr1










        
solution=Solution()
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
solution.relativeSortArray(arr1,arr2)

