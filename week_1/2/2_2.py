class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # m = 10
        # n = 2
        # strs = ["0001", "0001", "11"]
        
        less = "1" if m > n else "0"
        strs.sort( key = lambda val: val.count(less) )
        
        ret = 0
        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")
            
            if zeros <= m and ones <= n:
                m -= zeros
                n -= ones
                
                ret += 1
            
        return ret