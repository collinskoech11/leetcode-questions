#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3_head=ListNode(0)
        l3_curr=l3_head
        
        while list1 and list2:#assert both exist
            if list2.val < list1.val:
                l3_curr.next=list2#build l3's node
                list2 = list2.next
            else:
                l3_curr.next=list1
                list1 = list1.next
            l3_curr = l3_curr.next #find the next to build
        if list1:
            l3_curr.next= list1
        if list2:
            l3_curr.next = list2
        
        return l3_head.next
            
