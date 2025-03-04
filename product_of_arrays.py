class Solution(object):
    # Description:
    # Given an array of integers, find the product of all elements except arr[i] and replace arr[i] with it
    # Example: [1, 2, 3, 4] => [24, 12, 8, 6]
    # Must be O(n) complexity
    # Disclaimer: I have failed to finish this task using my own logic and python syntax knowledge in O(n) time.
    # I was only able to find a solution with O(n^2) minimum or with using the division sign(which was also prohibited)
    # The solution you are seeing below is the Leetcode solution with most upvotes
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Populate prefix and suffix with 1 n times
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer
            

sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
        

