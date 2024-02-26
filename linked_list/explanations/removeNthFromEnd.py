# Remove Nth Node From End of List

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

# This line defines a function named `removeNthFromEnd` that takes two parameters: `head` which is the head of a linked list, and `n` which is an integer.

    fast = slow = head

# This line initializes two pointers, `fast` and `slow`, to the head of the linked list.

    for _ in range(n):
        fast = fast.next

# This loop advances the `fast` pointer `n` nodes ahead in the linked list.

    if not fast:
        return head.next

# If `fast` is `None`, it means `n` is equal to the length of the linked list. So, the head of the list is the node to be removed. The function returns the second node as the new head of the list.

    while fast.next:
        fast = fast.next
        slow = slow.next

# This loop advances both `fast` and `slow` pointers until `fast` reaches the end of the list. At this point, `slow` will be at the `n`th node from the end of the list.

    slow.next = slow.next.next

# This line removes the `n`th node from the end of the list by skipping it in the `slow` pointer's link.

    return head

# Finally, the function returns the head of the modified list.