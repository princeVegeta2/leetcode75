class Solution(object):
    # Description:
    # Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
    # Any answer with a calculation error less than 10-5 will be accepted.
    # Example:
    # Input: nums = [1,12,-5,-6,50,3], k = 4
    # Output: Output: 12.75000
    # Use sliding window
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cur = best = sum(nums[:k])
        for i in range(k, len(nums)):
            cur = cur + nums[i] - nums[i - k]
            best = max(best, cur)
        # Must use float(best) in Python2
        return best / k


sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
        