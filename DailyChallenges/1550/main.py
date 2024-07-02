class Solution(object):
    def threeConsecutiveOdds(self, arr):
        is_odd=lambda x: x%2 !=0
        for i in range(len(arr)-2):
            if (is_odd(arr[i]) and is_odd(arr[i+1]) and is_odd(arr[i+2])):
                return True
        return False

        
solution=Solution()
arr = [2,6,4,1]
result=solution.threeConsecutiveOdds(arr)
print(result)
