# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


            fast = head 
            slow = head
            #find the mid point
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            #reverse the second part
            prev = None
            while slow:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
                    
            l, r = head, prev
                
            while r:
                if l.val != r.val:
                    return False
                l = l.next
                r = r.next
                    
            return True
            
            
            #         nums = []
#         while head:
#             nums.append(head.val)
#             head =  head.next
            
#         revnums = nums[::-1]
#         print(revnums)
#         if revnums == nums:
#             return True
#         else:
#             return False
