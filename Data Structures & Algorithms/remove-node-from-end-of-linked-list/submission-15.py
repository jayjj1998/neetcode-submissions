# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_count = 1
        curr = head
        while curr:
            if curr.next != None:
                curr = curr.next
            else:
                break
            node_count += 1

        if n == node_count:
            return head.next
        
        target = node_count - (n - 1)
        target_node = head
        for i in range(1, target - 1):
            if target_node:
                print(target_node.val)
                target_node = target_node.next
        if target_node and target_node.next:
            if target_node.next.next:
                target_node.next = target_node.next.next
            else:
                target_node.next = None
        
        return head