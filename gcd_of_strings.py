class Solution(object):
    # Description:
    # Return the greatest common divisor of two strings
    # Example: ABCABCABC, ABC => ABC
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        shortest_string = ""
        longest_string = ""

        if str1 < str2:
            shortest_string = str1
            longest_string = str2
        elif str1 > str2:
            shortest_string = str2
            longest_string = str1
        else:
            longest_string = str1
            shortest_string = str2
        
        if longest_string.replace(shortest_string, "") == "":
            return shortest_string
        
        gcd = shortest_string[:len(shortest_string) - 1]
        for i in range(len(gcd) -1, -1, -1):
            if shortest_string.replace(gcd, "") == "" and longest_string.replace(gcd, "") == "":
                return gcd
            gcd = gcd[:i]

        return gcd
    
    def bestSolutionLeetcode(self, str1, str2):
        # Euclidian algorithm
        if str1 + str2 != str2 + str1:
            # No same pattern
            return ""
        if len(str1) == len(str2):
            # Pattern exists and strings are the same, therefore both are correct, return any
            return str1
        if len(str1) > len(str2):
            # If the first string is bigger begin recursion for this case
            # Pass in the first string's slice starting at the last index of the second string(since its smaller)
            # and the whole second string
            # They will pass through the same checks and sooner or later on of them will trigger the second if statement or recursion again
            return self.bestSolutionLeetcode(str1[len(str2):], str2)
        # If str1 is not bigger than str2 then the opposite is true(previous IFs take care of equal case)
        # This time take the slice of the second(biggest) string starting at the last index of the first(smallest) string
        return self.bestSolutionLeetcode(str2[len(str1):], str1)
        

solution = Solution()
print(solution.gcdOfStrings("LEET", 
                            "CODE"))
                



        


