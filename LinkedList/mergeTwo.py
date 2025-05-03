#merging two sorted list
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
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
#function to merge two lists
def mergeTwoLists(list1,list2):
    curr=dummy=ListNode()
    while(list1 and list2):
        if(list1.val<list2.val):
            curr.next=list1
            list1=list1.next
        else:
            curr.next=list2
            list2=list2.next
        curr=curr.next
    if(list1==None or list2==None):
        curr.next=list1 if (list1) else list2
    return dummy.next
list1=ListNode()
list2=ListNode()
list1=build_linked_list([2,3,4,5])
list2=build_linked_list([8,9,10,11])
print_linked_list(list1)
print_linked_list(list2)
mhead=mergeTwoLists(list1,list2)
print_linked_list(mhead)