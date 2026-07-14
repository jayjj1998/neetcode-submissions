# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dic = {}
        curr = head
        n = 0
        while curr:
            dic[n] = curr
            curr = curr.next
            n += 1
        
        L, R = 0, len(dic) - 1
        while L < R:
            dic[L].next = dic[R]
            L+= 1
            if L >= R:
                break
            dic[R].next = dic[L]
            print(f"L {L}, R {R}")
            R -= 1
        
        dic[L].next = None