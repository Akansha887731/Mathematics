"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0
 
Constraints:
0 <= n <= 104
Follow up: Could you write a solution that works in logarithmic time complexity?
"""

"""
Intuition
We recognize that trailing zeros in a factorial result from the multiplication of 10, which is composed of 2 and 5. In a factorial calculation, the number of factors of 2 is usually more than the number of factors of 5. So, counting the factors of 5 gives us the count of trailing zeros.

Approach
Code uses a while loop to iteratively divide n by 5, adding the result to the count. This accounts for the factors of 5.

Complexity
Time complexity:
This approach has a time complexity of O(log n) because, in each iteration, the value of n is divided by 5, and the loop runs until n becomes zero.

Space complexity:
The space complexity of the code is O(1) or constant space. This is because the algorithm uses a single variable (count) to store the result and a loop variable (n) to iterate through the numbers.
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            n = n// 5
            count += n           
        return count
