class Solution(object):
    # Description:
    # Given a list of 0s and 1s where 1 means there is a flower, check whether the amount of flowers n can be placed fully
    # Constraint: cannot put flowers if adjacent indeces have '1', must be [0, 1, 0] for each flower
    # Example: flowerbed = [1,0,0,0,1], n = 1 => True
    # Example2: flowerbed = [1,0,0,0,1], n = 2 => False
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        checker = True

        # Edge case 1
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n <= 1:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] !=0 and n != 0:
            return False
        
        # Edge case 2
        if len(flowerbed) == 0:
            return False
        
        
        for i in range(len(flowerbed)):
            if i != len(flowerbed) - 1 and i != 0:
                if flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            elif i == 0 and flowerbed[i] != 1 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == len(flowerbed) - 1 and flowerbed[i] != 1 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
        if n > 0:
            checker = False
        
        return checker
    
    # Leetcode best
    def canPlaceFlowersLeet(self, flowerbed, n):
        # Edge case if no flowers need to be planted
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
    

sol = Solution()
print(sol.canPlaceFlowers([0,0,1,0,0], 1))
