# Reverse a Linked List

def reverseList(head: ListNode) -> ListNode:

# This line defines a function called `reverseList` that takes a `ListNode` as
# an argument and returns a `ListNode`. This function is intended to reverse a
# linked list.

    prev = None

# This line initializes a variable `prev` to `None`. This variable will be used
# to keep track of the previous node during the traversal of the linked list.

    current = head

# This line initializes a variable `current` to `head`, which is the starting
# node of the linked list.

    while current:

# This line starts a while loop that continues as long as `current` is not
# `None`. This is the main loop for traversing the linked list.

        next_node = current.next

# Inside the loop, this line saves the next node of `current` in the variable
# `next_node`. This is necessary because we are going to change `current.next`
# in the next line.

        current.next = prev

# This line reverses the link of the `current` node by pointing it to the `prev`
# node instead of the `next` node.

        prev = current

# This line moves the `prev` pointer one step forward to the `current` node.

        current = next_node

# This line moves the `current` pointer one step forward to the `next_node`,
# which was saved before.

    return prev

# After the loop ends (when `current` is `None`), the linked list has been
# reversed, and `prev` is now pointing to the new head of the reversed linked
# list. So, the function returns `prev`.