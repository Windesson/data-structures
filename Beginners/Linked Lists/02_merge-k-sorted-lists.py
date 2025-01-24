# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:     
        
        for i in range(1, len(lists)):
            if lists[i]:
                lists[0] = self.merge(lists[0], lists[i])

        return lists[0] if lists else None

    def merge(self, a, b)  -> Optional[ListNode]:
        dummy = ListNode()
        writer = dummy
        while a and b:
            if a.val < b.val:
                writer.next = a
                writer = a
                a = a.next
            else:
                writer.next = b
                writer = b
                b = b.next
        if a:
            writer.next = a
        else:
            writer.next = b

        return dummy.next