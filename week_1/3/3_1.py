class Solution:
    def longestValidParentheses(self, s: str) -> int:
    
        s = ")))))()"
        s = "()))(()"
        s = "))(("
        
        longest = 0
        opened = 0
        closed = 0
        
        for char in s:
            if char == "(":
                opened += 1
            else:
                closed += 1
            
            print(closed - opened)
            if closed - opened > 1:
                
                new_longest = min([opened, closed]) - 1
                print(new_longest)
                longest = new_longest if new_longest > longest else longest
                
                opened = 0
                closed = 0
            
        return longest
    