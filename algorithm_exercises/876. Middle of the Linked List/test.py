# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode):
        curr = curr2 = head
        while curr2 and curr2.next:
            curr = curr.next
            curr2 = curr2.next.next
        return curr

def test_middleNode():
    solver = Solution()
    elements = [1,2,3,4,5]
    head = ListNode(elements[-1])
    for val in reversed(elements):
        head.next = ListNode(val)
    
    assert Solution().middleNode() == [3,4,5]
