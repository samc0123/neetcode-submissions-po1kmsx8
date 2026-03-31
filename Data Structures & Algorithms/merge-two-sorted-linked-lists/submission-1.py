# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Get list 1 vals 
        vals1 = []
        while list1:
            vals1.append(list1.val)
            list1 = list1.next
        # Get list 2 vals 
        vals2 = []
        while list2:
            vals2.append(list2.val)
            list2 = list2.next
        vals_out = sorted(vals1+vals2)
        
        head = ListNode(val=vals_out[0]) if len(vals_out)>0 else None
        head_out = head # this is what is returned
        
        for i in range(1,len(vals_out)):
            # New node
            head.next = ListNode(val=vals_out[i])
            head = head.next
        
        return head_out

        