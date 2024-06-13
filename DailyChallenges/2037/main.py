class Solution(object):
    def minMovesToSeat(self, seats, students):
        count = 0 
        seats.sort()
        students.sort()
        for i in range(len(students)):
            count+=abs(students[i]-seats[i])
        print(count)
        









solution=Solution()
seats = [4,1,5,9]
students = [1,3,2,6]
solution.minMovesToSeat(seats,students)
