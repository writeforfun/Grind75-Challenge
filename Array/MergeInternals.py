'''
Title: 56. Merge Intervals
Level: Medium?
Link: https://leetcode.com/problems/merge-intervals/submissions/
Author: Yuan
Date: 2022/07/04
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if intervals == []:
            return []
        
        intervals = sorted(intervals)
        result = []
        
        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
                
        return result


