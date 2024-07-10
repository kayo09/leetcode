class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        current = head.next  # Skip the initial zero
        dummy = ListNode(0)
        tail = dummy
        current_sum = 0

        while current:
            if current.val != 0:
                current_sum += current.val
            else:
                # When we hit a zero, add the sum to the new list
                tail.next = ListNode(current_sum)
                tail = tail.next
                current_sum = 0  # Reset sum for the next segment
            current = current.next

        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next
        
solution=Solution()
head=[0,1,0,3,0,2,2,0]

solution.mergeNodes(head)

