class Solution(object):
    # Description:
    # Return a string by merging two string alternately
    # Example: ABC, QRS = AQBRCS
    def mergeAlternately(self, word1, word2):
    
        new_string = ""
        if len(word1) > len(word2):
            for i in range(0, len(word1)):
                if i == len(word2) - 1:
                    new_string += word1[i]
                    new_string += word2[i]
                    for j in range(len(word2), len(word1)):
                        new_string += word1[j]
                    break
                new_string += word1[i]
                new_string += word2[i]
        elif len(word1) < len(word2):
            for i in range(0, len(word1)):
                if i == len(word1) - 1:
                    new_string += word1[i]
                    for j in range(len(word1) - 1, len(word2)):
                        new_string += word2[j]
                    break
                new_string += word1[i]
                new_string += word2[i]
        else:
            for i in range(0, len(word1)):
                new_string += word1[i]
                new_string += word2[i]

        
        return new_string

solution = Solution()
print(solution.mergeAlternately("abcd", "pq"))