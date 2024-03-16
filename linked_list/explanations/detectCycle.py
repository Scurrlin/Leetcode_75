# Detect Cycle in a Linked List II

def detectCycle(head: ListNode) -> ListNode:

# This line defines a function named `detectCycle` that takes a `ListNode` as an
# argument and returns a `ListNode`. This function is used to detect if there's
# a cycle in a linked list.

    slow = fast = head

# This line initializes two pointers, `slow` and `fast`, at the head of the
# linked list.

    while fast and fast.next:

# This line starts a loop that continues as long as `fast` is not `None` and
# `fast.next` is not `None`. This is to prevent accessing `None.next` which
# would raise an error.

        slow = slow.next

# This line moves the `slow` pointer one step forward in the linked list.

        fast = fast.next.next

# This line moves the `fast` pointer two steps forward in the linked list.

        if slow == fast:

# This line checks if the `slow` pointer has met the `fast` pointer, which
# indicates a cycle in the linked list.

            slow2 = head

# If a cycle is detected, this line initializes a new pointer `slow2` at the
# head of the linked list.

            while slow != slow2:

# This line starts a new loop that continues as long as `slow` and `slow2` are
# not at the same node.

                slow = slow.next
                slow2 = slow2.next

# These lines move both `slow` and `slow2` one step forward in the linked list.

            return slow

# When `slow` and `slow2` meet, this line returns the node where they meet,
# which is the start of the cycle.

    return None

# If no cycle is detected, the function returns `None`.