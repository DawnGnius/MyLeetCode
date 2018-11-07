class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        row_indices = (list(range(numRows-1)) + list(range(numRows-1, 0, -1))) * (len(s) // numRows + 1)
        
        #assert len(row_indices) > len(s)
        
        for row_index, char in zip(row_indices, s):            
            rows[row_index] += char
                      
        return ''.join(rows)
