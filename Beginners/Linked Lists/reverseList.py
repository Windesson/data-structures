class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head;
        prev = None # None
        curr = head #[1]
        while curr:
            _next = curr.next # [2]
            curr.next = prev # [1].next -> None

            prev = curr  # [1]
            curr = _next # [2]

        return prev