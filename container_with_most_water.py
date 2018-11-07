class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        Note:
            1. Scan the list at list twice, Time Limit Exceeded. 
                for i in list:
                    for j in list:
                        cur_ area = min(list[i],list[j])*(j-i)
                        update max value
            2. It should be able to handle long lists and even large numbers. So we shell only scan the list once.
                It is easy to get the local min value.

        """
        i, j, area = 0, len(height)-1, 0
        while i != j:
            cur_area = min(height[i], height[j]) * (j-i)
            area = max(area, cur_area)
            if height[i] < height[j]: #Why this is correct?
                i += 1
            else:
                j -= 1
        return area