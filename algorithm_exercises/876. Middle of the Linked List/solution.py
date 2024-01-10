def middleNode(head):
    curr = curr2 = head
    while curr2 and curr2.next:
        curr = curr.next
        curr2 = curr2.next.next
    return curr
