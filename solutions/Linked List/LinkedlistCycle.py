# Given head, the head of a linked list, determine if the linked list has a cycle in it.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True

        return False
