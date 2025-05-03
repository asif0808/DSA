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
#Printing linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
#checking for cycle
def cycle(head):
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
    return False
obj=ListNode()
head=build_linked_list([3,2,0,-4])
print_linked_list(head)
print(cycle(head))