class Solution:
    def rob(self, nums: list[int]) -> int:
        # Edge case: If only one house exists, rob it directly.
        # Otherwise, compare excluding the last house vs. excluding the first house.
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2