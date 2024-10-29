class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Insertion at the end of a linked list
def insert(head, value):
    if head is None:
        return ListNode(value)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(value)
    return head

def printList(head):
    if head is not None:
        print(head.value)
        printList(head.next)

head = None
head = insert(head, 1)
head = insert(head, 2)
head = insert(head, 3)
head = insert(head, 4)
head = insert(head, 5)

printList(head)
