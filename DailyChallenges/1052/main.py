class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        #kadane
        prevSum=0
        note=0
        for i in range(len(customers)):
            j=1
            currSum=0
            while j <=minutes and i+j<len(customers):
                currSum+=customers[i+j]
                if(currSum>prevSum) :
                    prevSum=currSum
                    note=i
                j+=1


            print(prevSum)
        print(note)




solution=Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes=3
solution.maxSatisfied(customers,grumpy,minutes)