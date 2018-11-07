class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num2str_map = {"0":None, "1":None, "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pgrs", "8":"tuv", "9":"wxyz"}
        str = []
        for num in digits:
            n = len(num2str_map[num])
            str *= n
            if str == []:
                for j in num2str_map[num]:
                    str.append(j)
            else:
                for i in range(len(str)):
                    str[i] += num2str_map[num][i//int(len(str)/n)]
            # print(str)
        return str

A = Solution()
print(A.letterCombinations("234"))

