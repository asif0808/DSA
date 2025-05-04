class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
#creating a linkdlist
def build_linked_list(values):
    if not values:
        return None
    head=ListNode(values[0])
    curr=head
    for val in values[1:]:
        curr.next=ListNode(val)
        curr=curr.next
    return head
#print linkedlist
def print_linked_list(head):
    if not head:
        return None
    curr=head
    while(curr!=None):
        print(curr.val,'->',end='')
        curr=curr.next
    print(curr)

#function to delete nth node from end of the list
#BRUTE-FORCE APPROACH
# def DeleteN(head,n):
#     count=0
#     curr=head
#     while curr:
#         count+=1
#         curr=curr.next
#     # print(count)
#     if(count==n):
#         newHead=head.next
#         return newHead
#     temp=head
#     res=count-n
#     while temp:
#         res-=1
#         if(res==0):
#             break
#         temp=temp.next
#     temp.next=temp.next.next
#     return head
    
#OPTIMAL SOLUTION
def DeleteNthNode(head,n):
    slow=head
    fast=head
    for _ in range(n):
        if fast:
            fast=fast.next
    if(fast==None):
        newHead=head.next
        return newHead
    while fast.next:
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next
    return head

            


obj=ListNode()
head=build_linked_list([2,3,4,5,9,6])
print_linked_list(head)
#head=DeleteN(head,3)
head=DeleteNthNode(head,3)
print_linked_list(head)
#head=DeleteN(head,5)
head=DeleteNthNode(head,5)
print_linked_list(head)