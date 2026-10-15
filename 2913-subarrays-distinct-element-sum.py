# LeetCode: 2913 - Subarrays Distinct Element Sum of Squares I
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

# Your accepted solution goes here


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i,n):
                seen.add(nums[j])

                distinct = len(seen)
                total += distinct * distinct
        return total