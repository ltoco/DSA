'''
lets say we have 2 arrays a1 = [a,b] and a2 = [c,d]
Intervals can be merged if a1[0] < a2[0] => this is acheived by sorting the intervals
Intervals can be merged if a2[0] < a1[1]
'''

class Solution:
    def merge(self, intervals):
        intervals.sort(key =lambda x: x[0])
        merged = []
        for i in intervals:
            # if the list of merged intervals is empty 
            # or if the current interval does not overlap with the previous,
            # simply append it.
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
            # otherwise, there is overlap,
            #so we merge the current and previous intervals.
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
            print(merged)
        return merged

if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 5], [2, 3], [4, 8], [9, 10]]
    print(s.merge(intervals))