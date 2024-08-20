class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        count=0
        for i in range(len(seats)):
            count=count+abs(seats[i]-students[i])
        return count           