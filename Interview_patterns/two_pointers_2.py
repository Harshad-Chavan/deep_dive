class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Helper function to create a linked list from list
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# Helper to print linked list from a node
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create list: 1 -> 2 -> 3 -> 4 -> 5
head = create_linked_list([1, 2, 3, 4, 5])

# Find middle node
middle = middleNode(head)

# Print from middle
print_linked_list(middle)
