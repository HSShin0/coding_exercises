'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        time/space complexity : O(n^2) / O(n) where n = len(intervals)
        '''   
        if not intervals:
            return []
        
        # sort the intervals so that [ [x0, y0], [x1, y1], ...] with x0 <= x1 ....
        intervals.sort()  # time complexity O(nlogn)?
        
        answer = []
        i = 0
        while True:
            x, y = intervals[i]
            # if the last interval is disjoint with others
            if i == len(intervals) - 1:
                answer.append([x, y])
                return answer
            
            y_max = y
            for j in range(i+1, len(intervals)):
                x_, y_ = intervals[j]
                # if overlaps
                if x_ <= y_max:
                    if y_ > y_max:
                        y_max = y_
                    # if the last interval is not disjoint with others
                    if j == len(intervals) - 1:
                        answer.append([x, y_max])
                        return answer
                else:
                    # new interval start from x_
                    i = j
                    break
            
            answer.append([x, y_max])
