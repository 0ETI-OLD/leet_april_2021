longest = 0
        
        for index1 in range(0, len(s)):
            val1 = s[index1]
            
            count_open = 0
            count_close = 0
            
            for index2 in range(index1, len(s)):
                val2 = s[index2]
                count_open += 1 if val2 == "(" else 0
                count_closed += 1 if val2 == ")" else 0
                
                if count_closed > count_opened:
                    new_longest = index2 - index1
                    longest = new_longest if new_longest > longest else longest
                    
                    break
                    
            
                    
            
            
        return longest