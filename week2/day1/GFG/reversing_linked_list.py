'''

Reverse a linked list

Problem Statement:
Given the head of a linked list, the task is to reverse this list and return the reversed head.

Example:
Input: head: 1 -> 2 -> 3 -> 4 -> NULL
Output: head: 4 -> 3 -> 2 -> 1 -> NULL

Solution:
function reverseList(self, head) is the solution function.

Class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None
'''

# Given the head of a list, reverse the list and return the
# head of reversed list
def reverseList(head):

    # Iterative Python program to reverse a linked list

    curr = head
    prev = None

    # Traverse all the nodes of Linked List
    while curr is not None:

        # Store next
        nextNode = curr.next

        # Reverse current node's next pointer
        curr.next = prev

        # Move pointers one position ahead
        prev = curr
        curr = nextNode

    # Return the head of reversed linked list, which is the last node of the list before reversing.
    return prev

# Time complexity: O(n)
# Space complexity: O(1)