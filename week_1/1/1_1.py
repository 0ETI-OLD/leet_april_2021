import math

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        is_palindrome = False
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
            
        first_half = None
        second_half = None
        
        first_half = vals[:math.floor(len(vals) / 2)]
        second_half = vals[math.ceil(len(vals) / 2):]
        
        # print(first_half)
        # print(second_half)
        
        for index, val in enumerate(first_half):
            # print(val, second_half[-(index+1)])
            if val != second_half[-(index+1)]:
                return False
        
        return True