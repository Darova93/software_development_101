def middleNode(head):
    slowPointer = head
    fastPointer = head
    while fastPointer and fastPointer.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    return slowPointer
