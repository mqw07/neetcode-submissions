# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Pre(l1, l2) -> l1, l2 are sorted ll, 0 <= len(l1), len(l2) <= 100

        Need to return l3 in all linkedlist s.t. Post(l3) l3 contains all nodes in 
        l1 and l2, and l3 is sorted.

        Strategy:
        Find the smaller ll head value out of l1, l2. Use this list to
        iterate through each following values of both l1 and l2, linking the 
        prev value to the next smallest value
        """

        if not list1:
            return list2
        if not list2:
            return list1
        # Both lists are non-empty

        if head1.val > head2.val:
            start = head2
            other = head1
        else:
            start = head1
            other = head2
        
        curr1 = start
        curr2 = other

        while curr1.next and curr2: 
            # Link the current node to the next smallest node
            if curr1.next.val > curr2.val:
                temp = curr1.next
                curr1.next, curr2 = curr2, curr2.next
                curr1.next.next = temp
            else:
                curr1 = curr1.next

        if not curr1.next and curr2:
            curr1.next = curr2

        return start 


        