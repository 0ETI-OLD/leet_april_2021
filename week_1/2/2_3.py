class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
#         strs = ["0000111","0000111111","01111111","0001","000111111","0000001111111","00011111","000011111","00000011","0111111","0000000001111111","0011","001111","00000001111","0011","0000111111111","0001111111","011111111"]
        
#         m = 4
#         n = 6
        
        
        # First Type of Sort by Length
        # strs.sort( key = lambda val: len(val) )
        # ret1 = self.getRetVal(strs, m, n)
        
        # Second Type of Sort by #0's
        strs.sort( key = lambda val: (len(val), val.count("0")) )
        ret2 = self.getRetVal(strs, m, n)
        
        # Third Type of Sort by #1's
        strs.sort( key = lambda val: (len(val), val.count("1")) )
        ret3 = self.getRetVal(strs, m, n)
        
        # Fourth Type of Sort by #0's
        strs.sort( key = lambda val: (val.count("0")) )
        ret4 = self.getRetVal(strs, m, n)
        
        # Fifth Type of Sort by #1's
        strs.sort( key = lambda val: (val.count("1")) )
        ret5 = self.getRetVal(strs, m, n)
        
        return max([ ret2, ret3, ret4, ret5])
    
    def getRetVal(self, strs, m, n):
        ret = 0
        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")
            
            if zeros <= m and ones <= n:
                m -= zeros
                n -= ones
                
                ret += 1
            
        return ret