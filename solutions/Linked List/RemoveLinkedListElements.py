# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev,curr = dummy,head
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr=nxt
        return dummy.next
