class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#function to create linkedlist
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
#function to convert linkedlist to reverse
def mylist(head):
    prev=None
    curr=head
    next=None
    while(curr!=None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev
#Printing linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
obj=ListNode()
head=build_linked_list([2,3,4,5,6])
print_linked_list(head)
head=mylist(head)
print_linked_list(head)
