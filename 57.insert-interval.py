from typing import List

#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (32.46%)
# Likes:    1246
# Dislikes: 144
# Total Accepted:    217.5K
# Total Submissions: 669.8K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Merges intervals
        def merge2(x, y):
            m2 = []
            if x[0] > y[0]: x,y = y,x
            # 1. no overlap
            if x[1] < y[0]:
                m2 = [x, y]
            # 2. full overlap
            elif x[0] <= y[0] and y[1] <= x[1]:
                m2 = [x]
            # 2. partial overlap
            elif x[0] <= y[0] <= x[1]:
                m2 = [[x[0], y[1]]]
            #print("Merged two intervals ", x, y, m2)
            return m2

        # Merges 3 sorted intervals
        def merge3(x, y, z):
            m2 = merge2(x, y)
            m3 = []
            if len(m2) == 1:
                m3 = merge2(m2[0], z)
            else:
                m3 = [m2[0]] + merge2(m2[1], z)
            #print("Merged three intervals ", x, y, z, m3)
            return m3

        # Finds floor interval
        def findMergeInterval(intervals, val):
            start = 0
            end = len(intervals)-1
            res = 0
            while start <= end:
                mid = (start + end) // 2
                if intervals[mid][0] <= val:
                    res = mid
                    start = mid + 1
                else:
                    end = mid - 1
            #print("Found merge interval index for ", val, " to be ", res)
            return res

        # Intervals are non-overlapping
        sz = len(intervals)
        if not sz:
            return [newInterval]
        start = findMergeInterval(intervals, newInterval[0])
        end = findMergeInterval(intervals, newInterval[1])
        # TODO: simplify using mergeN
        if start == end:
            m3 = merge2(newInterval, intervals[start])
        else:
            m3 = merge3(intervals[start], newInterval, intervals[end])
        return intervals[:start] + m3 + intervals[end+1:]

# @lc code=end
