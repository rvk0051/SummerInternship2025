# Given an array arr[][] such that arr[i][0] is the starting time of ith meeting and
# arr[i][1] is the ending time of ith meeting, the task is to check if it is possible for a person
# to attend all the meetings such that he can attend only one meeting at a particular time.

# Note: A person can attend a meeting if
# its starting time is greater than or equal to the previous meeting's ending time.

# Example:-
# Input: arr[][] = [[1, 4], [10, 15], [7, 10]]
# Output: true
# Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings.

def canAttend(self, arr):

    meetings = sorted(arr)
    # 'meetings' stores the meeting time of all meetings in sorted order

    no_of_meetings = len(meetings)

    for meeting_no in range(0, no_of_meetings - 1):
        # checking time of all meetings
        # if the ending time of a meeting is greater than the starting time of the next meeting,
        # then one of the meetings can't be attended, hence returning false

        if meetings[meeting_no + 1][0] < meetings[meeting_no][1]:
            return False
#if the function is not returned false till, that means all meetings can be attended, hence returning true.
    return True

# Time Complexity':- O(n log n)  due to sorting
# Space Complexity:- O(n)  due to making a new array and storing sorted array