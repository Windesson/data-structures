# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy= ListNode()
        writer = dummy

        while len(lists) > 0:

            #remove None
            for i in range(len(lists) -1, -1, -1):
                if not lists[i]:
                    lists.pop(i)

            #check if still valid
            if not lists:
                break

            #find lowest val
            candidateNodeIndex = 0
            for i in range(len(lists)):
                tmp = lists[i]
                if tmp.val < lists[candidateNodeIndex].val:
                        candidateNodeIndex = i

            # add to the response
            writer.next = lists[candidateNodeIndex]
            writer = writer.next 

            #update the list
            lists[candidateNodeIndex] = lists[candidateNodeIndex].next
        
        return dummy.next
            
            
        