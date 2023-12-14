"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_count = 1
        if len(points) == 1:
            return max_count
        for i in range(len(points)-1):
            slope = {}
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]

                if x1 == x2:
                    m = float('inf')  # Handle vertical lines
                else:
                    m = (y2 - y1) / (x2 - x1)

                if m in slope:
                    slope[m] += 1
                else:
                    slope[m] = 1
            max_count = max(max_count, max(slope.values()))

        return max_count + 1
