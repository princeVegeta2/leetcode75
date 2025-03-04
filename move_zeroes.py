class Solution(object):
    def moveZeroes(self, nums):
        # Description:
        # Given a list of integers, move zeroes to the end whilist keeping the existing order of nums
        # Rules:
        # Modify an existing list, not create a new one
        # Note: I am returning nums here for the sake of testing
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums[i]) 
                nums.remove(nums[i])
        
        return nums
    
    # Leetcode best
    def moveZeroes(self, nums):

        non_zero = 0  # Pointer for non-zero elements
        
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
    

sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))


        