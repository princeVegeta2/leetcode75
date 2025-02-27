class Solution(object):
    # Description
    # For each element of the array of numbers, check if adding extraCandies to c in candy will result in the largest value in the list
    # Example:
    # [2, 3, 5, 1, 3], 3 => [True, True, True, False, True]
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        answers = []
        for i in range(len(candies)):
            checker = True
            for c in candies:
                if c > candies[i] + extraCandies:
                    checker = False
                    break
            answers.append(checker)

        return answers
    
    # Best solution on leetcode
    def kidsWithCandies(self, candies, extraCandies):
        # Finds the largest candy element
        max_candies = max(candies)
        
        result = []
        
        for candy in candies:
            # Self explanatory
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))