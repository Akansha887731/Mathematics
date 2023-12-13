"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
Constraints:
0 <= x <= 231 - 1
"""


"""
Intuition
The problem is to find the square root of a given non-negative integer x. Instead of using an exhaustive linear search, the code uses binary search to efficiently narrow down the possible range where the square root might be found.

Approach
If x is 0 or 1, the square root is x. This is handled by the initial check.
Initialize left to 1 and right to x // 2. This is because the square root of x cannot be greater than x // 2 for x > 1.
Perform a binary search within the range [left, right] to find the square root.
The variable res keeps track of the last valid result (floor value of the square root).
Update the left and right pointers based on the comparison of the square of the midpoint (mid * mid) with x.

Complexity

Time complexity:
The time complexity of this algorithm is O(log(x)). This is because the binary search reduces the search space by half in each iteration, and the search space is limited to the range [1, x // 2].

Space complexity:
The space complexity is O(1) or constant. The algorithm uses a constant amount of space for variables like left, right, res, and mid, regardless of the input size.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        left = 1
        right = x // 2
        res = 0
        while left <= right:
            mid = left + ((right-left)//2)
            value = mid * mid
            if value == x:
                return mid
            elif value > x:
                right = mid - 1
            else:
                left = mid + 1
                res = mid
        return res
