# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:     
        
        interval = 1
        nodes = len(lists)
        while interval < nodes:
            for i in range(0, nodes - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if lists else None

    def merge(self, l1, l2)  -> Optional[ListNode]:
        dummy = ListNode()
        point = dummy
        while l1 and l2:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next

        if l1:
            point.next = l1
        else:
            point.next = l2

        return dummy.next


            
            
        