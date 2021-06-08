# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num_list = []
        curr = head
        while curr:
            num_list.append(curr.val)
            curr = curr.next
        return num_list == num_list[::-1]