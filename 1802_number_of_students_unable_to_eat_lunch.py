class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count_students = Counter(students)

        for sandwich in sandwiches:
            if count_students[sandwich] == 0:
                return count_students[0] + count_students[1]

            count_students[sandwich] -= 1

        return 0