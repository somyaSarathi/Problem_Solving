class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sorting intervals wrt to starting* time
        intervals = sorted(intervals, key=lambda x: x[0])
        
        i = 1
        while i < len(intervals):
            if intervals[i-1][0] == intervals[i][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
                del intervals[i-1]
                
            elif intervals[i-1][1] >= intervals[i][1]:
                intervals[i][0] = min(intervals[i][0], intervals[i-1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
                del intervals[i-1]
                
            elif intervals[i-1][1] >= intervals[i][0]:
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
                del intervals[i-1]
                
            else: i+=1
                
        return intervals
