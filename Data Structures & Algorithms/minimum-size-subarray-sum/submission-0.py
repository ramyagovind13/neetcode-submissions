class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        tot = 0
        length = float("inf")
        for r in range(len(nums)):
            tot += nums[r]
            while tot >= target:
                length = min(length, r-l+1)
                tot -= nums[l]
                l += 1
        return length if length != float("inf") else 0