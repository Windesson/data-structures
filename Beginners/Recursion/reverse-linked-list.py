class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def ToList(self):
        temp = [self.val]
        next = self.next
        while next:
            temp.append(next.val)
            next = next.next;
        return temp;

def reverseList(head):
    # null 1 -> 2 -> null
    # null <-1 2->null
    # null <- 1 <- 2
    prev = None
    curr = head # 1
    while curr:
        temp = curr.next #2
        curr.next = prev

        prev = curr #1
        curr = temp #2

    return prev


#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
def testCase1():
    head = ListNode(1)
    curr = head
    for i in range(2,6):
        curr.next = ListNode(i)
        curr = curr.next

    expectedOut = [5,4,3,2,1]
    actualOut = reverseList(head)

    if actualOut.ToList() == expectedOut:
        print("Test case 1: pass")
    else:
        print("Test case 1: failed")

testCase1()