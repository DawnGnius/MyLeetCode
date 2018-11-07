class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int 
        initicalization
            sign = 1
            re_x = 0
        get sign
        special case
            0
        remove 0s at the end of x
        reverse remains of x
        """
        #Initialization
        sign = 1
        re_x = 0
        #Get sign
        if x < 0:
            sign = -1
            x = -1 * x
        #Special case
        if x == 0:
            return 0
        #Remove 0s
        while x%10 == 0:
            x = x // 10
        #Reverse x
        while x != 0:
            re_x = re_x * 10 + x % 10
            x = x //10
            if re_x > 2 ** 31: #Bound areas
                return 0
        return re_x * sign