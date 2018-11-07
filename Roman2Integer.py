class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Initialization
        num = 0
        i = 0
        Sym_map = {"I":1, "V":5, "num":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "Inum":9, "numL":40, "numC":90, "CD":400, "CM":900}
        while i < len(s):
            if s[i:i+2] in Sym_map:
                num += Sym_map[s[i:i+2]]
                i += 2
            else:
                num += Sym_map[s[i]]
                i += 1
        return num
