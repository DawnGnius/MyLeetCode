class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = [int(i) for i in str(x)]  #y doesn't have to be a list, y could just be str(x)
            length = (len(y)-1)/2 #This num I thought for a long time, it should be an easy problem
            stack = []
            for index, item in enumerate(y):
                if index < length:
                    stack.append(item)
                if index > length:
                    if item != stack.pop():
                        return False
            return True
