#damn i gotta git beddar :(
class Solution(object):
    def canBeEqual(self, target, arr):
        for i in range(len(arr)):
            
            while(arr[i]<arr[(i+1)%len(arr)]):
                temp=arr[i]
                arr[i]=arr[(i+1)%len(arr)]
                arr[(i+1)%len(arr)]=temp

            print(arr)
                
        
solution=Solution()
target = [1,2,3,4] 
arr = [2,4,1,3]
solution.canBeEqual(target,arr)
